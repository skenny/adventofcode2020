INPUT_FILE = "day10-input"
TEST_INPUT_FILE_1 = "day10-input-test"
TEST_INPUT_FILE_2 = "day10-input-test-2"

DEVICE_ADAPTER_JOLTAGE_ADJ = 3

def read_input(file):
    with open(file, "r") as fin:
        return [int(l) for l in fin.readlines()]

def plug_in(adapters):
    joltage = 0
    deltas = []
    while len(adapters) > 0:
        adapter = min(list(filter(lambda adapter_joltage: adapter_joltage - joltage <= 3, adapters)))        
        adapters.remove(adapter)
        deltas.append(adapter - joltage)
        joltage = adapter

    joltage += DEVICE_ADAPTER_JOLTAGE_ADJ
    deltas.append(DEVICE_ADAPTER_JOLTAGE_ADJ)

    return deltas.count(1) *  deltas.count(3)

def run(label, file):
    adapters = read_input(file)
    print("{} 1: {}".format(label, plug_in(adapters)))

run("test 1", TEST_INPUT_FILE_1)
run("test 2", TEST_INPUT_FILE_2)
run("part", INPUT_FILE)
