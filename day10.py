INPUT_FILE = "day10-input"
TEST_INPUT_FILE_1 = "day10-input-test"
TEST_INPUT_FILE_2 = "day10-input-test-2"

DEVICE_ADAPTER_JOLTAGE_ADJ = 3
MAX_JOLTAGE_DIFFERENCE = 3
OUTLET_JOLTAGE = 0

def read_input(file):
    with open(file, "r") as fin:
        return [int(l) for l in fin.readlines()]

def connect(adapters):
    joltage = OUTLET_JOLTAGE
    deltas = []
    while len(adapters) > 0:
        adapter = min(list(filter(lambda adapter_joltage: adapter_joltage - joltage <= MAX_JOLTAGE_DIFFERENCE, adapters)))
        adapters.remove(adapter)
        deltas.append(adapter - joltage)
        joltage = adapter

    # account for built in adapter joltage
    joltage += DEVICE_ADAPTER_JOLTAGE_ADJ
    deltas.append(DEVICE_ADAPTER_JOLTAGE_ADJ)

    return deltas.count(1) *  deltas.count(3)

def run(label, file):
    adapters = read_input(file)
    print("{} 1: {}".format(label, connect(adapters)))

run("test 1", TEST_INPUT_FILE_1)
run("test 2", TEST_INPUT_FILE_2)
run("part", INPUT_FILE)
