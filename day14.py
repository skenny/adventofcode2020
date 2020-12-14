import re

INPUT_FILE = "day14-input"
TEST_INPUT_FILE = "day14-input-test"

def read_input(file):
    with open(file, "r") as fin:
        return [l.strip() for l in fin.readlines()]

def int_to_bit_field(i):
    return [1 if digit == "1" else 0 for digit in bin(i)[2:]]

def bit_field_to_int(bits):
    return int("".join(str(i) for i in bits), 2)

def part1(program):
    bit_mask = ['0'] * 36
    mem = {}
    for line in program:
        if line.startswith("mask"):
            bit_mask = list(line.split(" = ")[1])
            bit_mask.reverse()
            #print("using mask", bit_mask)
        if line.startswith("mem"):
            search_result = re.search(r"mem\[(\d+)\] = (\d+)", line)
            if search_result:
                address = search_result.group(1)
                value = int(search_result.group(2))
                bit_value = int_to_bit_field(value)
                bit_value.reverse()
                masked_bit_value = []
                for i, mask_bit in enumerate(bit_mask):
                    v = bit_value[i] if i < len(bit_value) else 0
                    new_bit_value = v
                    if mask_bit != "X":
                        new_bit_value = int(mask_bit)
                    masked_bit_value.insert(0, new_bit_value)
                #print("masked", bit_value, "->", masked_bit_value)
                mem[address] = bit_field_to_int(masked_bit_value)
    return sum(mem.values())

def run(label, input_file):
    input = read_input(input_file)
    print("{} 1: {}".format(label, part1(input)))

run("test", TEST_INPUT_FILE)
run("part", INPUT_FILE)