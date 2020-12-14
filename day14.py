import re

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
    aaa = int_to_bit_field(value)
    bit_value = list(reversed(aaa))
    masked_bit_value = []

    for i, mask_bit in enumerate(reversed(bit_mask)):
        new_bit_value = bit_value[i] if i < len(bit_value) else 0
        if mask_bit != "0":
            new_bit_value = mask_bit
        masked_bit_value.insert(0, new_bit_value)

    masked_values = []
    # TODO generate all possible values by replacing Xs with 0/1

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
#run("part", INPUT_FILE)