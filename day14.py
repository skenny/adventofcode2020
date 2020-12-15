import re
import itertools

INPUT_FILE = "day14-input"
TEST_INPUT_FILE_1 = "day14-input-test"
TEST_INPUT_FILE_2 = "day14-input-test-2"

def read_input(file):
    with open(file, "r") as fin:
        return [l.strip() for l in fin.readlines()]

def int_to_bit_field(i):
    return [1 if digit == "1" else 0 for digit in bin(i)[2:]]

def bit_field_to_int(bits):
    return int("".join(str(i) for i in bits), 2)

def apply_mask1(value, bit_mask):
    bit_value = list(reversed(int_to_bit_field(value)))
    masked_bit_value = []

    for i, mask_bit in enumerate(reversed(bit_mask)):
        new_bit_value = bit_value[i] if i < len(bit_value) else 0
        if mask_bit != "X":
            new_bit_value = int(mask_bit)
        masked_bit_value.insert(0, new_bit_value)

    return bit_field_to_int(masked_bit_value)

def apply_mask2(value, bit_mask):
    bit_value = list(reversed(int_to_bit_field(value)))
    masked_bit_value = []

    for i, mask_bit in enumerate(reversed(bit_mask)):
        new_bit_value = bit_value[i] if i < len(bit_value) else 0
        if mask_bit != "0":
            new_bit_value = mask_bit
        masked_bit_value.insert(0, new_bit_value)

    aaa = "".join(str(i) for i in masked_bit_value)
    num_floating = aaa.count("X")

    #print(masked_bit_value)
    
    floating_permutations = []
    floating_permutations.append(list("0" * num_floating))
    floating_permutations.append(list("1" * num_floating))
    for i in range(1, num_floating):
        base = "".join(["1"] * i).zfill(num_floating)
        [floating_permutations.append(l) for l in list(itertools.permutations(base))]

    #print(floating_permutations)

    masked_values = []
    for fp in floating_permutations:
        address = aaa
        for i in fp:
            address = address.replace("X", i, 1)
        masked_values.append(bit_field_to_int(address))
    
    #print(masked_values)

    return masked_values

def part1(program):
    bit_mask = ['0'] * 36
    mem = {}
    for line in program:
        if line.startswith("mask"):
            bit_mask = list(line.split(" = ")[1])
        if line.startswith("mem"):
            search_result = re.search(r"mem\[(\d+)\] = (\d+)", line)
            if search_result:
                address = int(search_result.group(1))
                value = int(search_result.group(2))
                mem[address] = apply_mask1(value, bit_mask)
    return sum(mem.values())

def part2(program):
    bit_mask = ['0'] * 36
    mem = {}
    for line in program:
        if line.startswith("mask"):
            bit_mask = list(line.split(" = ")[1])
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