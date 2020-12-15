import re
import itertools

INPUT_FILE = "day14-input"
TEST_INPUT_FILE_1 = "day14-input-test"
TEST_INPUT_FILE_2 = "day14-input-test-2"

def read_input(file):
    with open(file, "r") as fin:
        return [l.strip() for l in fin.readlines()]

def int_to_bit_field(i):
    return bin(i)[2:].zfill(36)

def bit_field_to_int(bits):
    return int(bits, 2)

def apply_mask1(value, bit_mask):
    bit_value = int_to_bit_field(value)
    masked_bits = list(bit_value)
    for i, mask_bit in enumerate(list(bit_mask)):
        masked_bits[i] = mask_bit if mask_bit != "X" else bit_value[i]
    return bit_field_to_int("".join(masked_bits))

def apply_mask2(value, bit_mask):
    bit_value = int_to_bit_field(value)
    masked_bits = list(bit_value)
    floating_indices = []
    for i, mask_bit in enumerate(list(bit_mask)):
        masked_bits[i] = mask_bit if mask_bit != "0" else bit_value[i]

        # keep track of floating bit indexes for replacement later
        if mask_bit == "X":
            floating_indices.append(i)

    num_floating = len(floating_indices)
    
    floating_permutations = []
    floating_permutations.append("".join("0" * num_floating))
    floating_permutations.append("".join("1" * num_floating))
    for i in range(1, num_floating):
        base = "".join("1" * i).zfill(num_floating)
        [floating_permutations.append("".join(l)) for l in list(itertools.permutations(base))]

    masked_values = []
    for fp in floating_permutations:
        #print(masked_bits, floating_indices, fp)
        for i, b in enumerate(list(fp)):
            masked_bits[floating_indices[i]] = b
        masked_values.append(bit_field_to_int("".join(masked_bits)))
    
    #print(masked_values)

    return masked_values

def part1(program):
    bit_mask = "0" * 36
    mem = {}
    for line in program:
        if line.startswith("mask"):
            bit_mask = line.split(" = ")[1]
        if line.startswith("mem"):
            search_result = re.search(r"mem\[(\d+)\] = (\d+)", line)
            if search_result:
                address = int(search_result.group(1))
                value = int(search_result.group(2))
                mem[address] = apply_mask1(value, bit_mask)
    return sum(mem.values())

def part2(program):
    bit_mask = "0" * 36
    mem = {}
    for i, line in enumerate(program):
        print(i, line)
        if line.startswith("mask"):
            bit_mask = line.split(" = ")[1]
        if line.startswith("mem"):
            search_result = re.search(r"mem\[(\d+)\] = (\d+)", line)
            if search_result:
                address = int(search_result.group(1))
                value = int(search_result.group(2))
                for address in apply_mask2(address, bit_mask):
                    mem[address] = value
    return sum(mem.values())

def run(label, input_file1, input_file2):
    print("{} 1: {}".format(label, part1(read_input(input_file1))))
    print("{} 2: {}".format(label, part2(read_input(input_file2))))

run("test", TEST_INPUT_FILE_1, TEST_INPUT_FILE_2)
run("part", INPUT_FILE, INPUT_FILE)