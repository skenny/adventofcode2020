INPUT_FILE = "day8-input"

def read_input():
    with open(INPUT_FILE, "r") as fin:
        return [l.strip() for l in fin.readlines()]

def parse_boot_code(input):
    boot_code = []
    for i in input:
        op, arg = i.strip().split(" ")
        boot_code.append({ "op": op, "arg": int(arg) })
    return boot_code

def execute(boot_code):
    accumulator = 0
    instr_ptr = 0
    loop = False

    for instr in boot_code:
        instr["executed"] = False

    while True:
        if instr_ptr < 0 or instr_ptr >= len(boot_code):
            print("exit: instr_ptr is out of range: {} (0..{})".format(instr_ptr, len(boot_code) - 1))
            break

        instr = boot_code[instr_ptr]
        op = instr["op"]
        arg = instr["arg"]
        executed = instr["executed"]

        if executed:
            #print("already executed instruction {}; aborting...".format(instr_ptr))
            loop = True
            break
        
        instr["executed"] = True

        if (op == "acc"):
            accumulator += arg
            instr_ptr += 1
        elif (op == "jmp"):
            instr_ptr += arg
        elif (op == "nop"):
            instr_ptr += 1

    return (accumulator, loop)

def repair(boot_code):
    for instr in boot_code:
        if (instr["op"] == "nop"):
            instr["op"] = "jmp"
            result = execute(boot_code)
            if not result[1]:
                return result
            instr["op"] = "nop"
        if (instr["op"] == "jmp"):
            instr["op"] = "nop"
            result = execute(boot_code)
            if not result[1]:
                return result
            instr["op"] = "jmp"

def run_tests():
    test_boot_code = parse_boot_code([
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ])
    print("test 1", execute(test_boot_code))
    print("test 2", repair(test_boot_code))

def run_parts():
    boot_code = parse_boot_code(read_input())
    print("part 1", execute(boot_code))
    print("part 2", repair(boot_code))

run_tests()
run_parts()