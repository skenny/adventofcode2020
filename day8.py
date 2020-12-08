INPUT_FILE = "day8-input"

def read_input():
    with open(INPUT_FILE, "r") as fin:
        return [l.strip() for l in fin.readlines()]

def parse_boot_code(input):
    boot_code = []
    for i in input:
        op, arg = i.strip().split(" ")
        boot_code.append({ "op": op, "arg": int(arg), "executed": False})
    return boot_code

def execute(boot_code):
    accumulator = 0
    instr_ptr = 0

    while True:
        if instr_ptr < 0 or instr_ptr >= len(boot_code):
            #print("instr_ptr is out of range: {} (boot code has {} instructions)".format(instr_ptr, len(boot_code)))
            break

        instr = boot_code[instr_ptr]
        op = instr["op"]
        arg = instr["arg"]
        executed = instr["executed"]

        if executed:
            #print("already executed instruction {}; aborting...".format(instr_ptr))
            break
        
        instr["executed"] = True

        if (op == "acc"):
            accumulator += arg
            instr_ptr += 1
        elif (op == "jmp"):
            instr_ptr += arg
        elif (op == "nop"):
            instr_ptr += 1

    return accumulator

def run_tests():
    input = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ]
    test_boot_code = parse_boot_code(input)
    final_acc = execute(test_boot_code)
    print("test", final_acc)

def run_parts():
    boot_code = parse_boot_code(read_input())
    print("part 1", execute(boot_code))

run_tests()
run_parts()