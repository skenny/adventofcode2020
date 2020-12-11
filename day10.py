INPUT_FILE = "day10-input"
TEST_INPUT_FILE_1 = "day10-input-test"
TEST_INPUT_FILE_2 = "day10-input-test-2"
TEST_INPUT_FILE_3 = "day10-input-test-3"

DEVICE_ADAPTER_JOLTAGE_ADJ = 3
MAX_JOLTAGE_DIFFERENCE = 3
OUTLET_JOLTAGE = 0

def read_input(file):
    with open(file, "r") as fin:
        return [int(l) for l in fin.readlines()]

def connect(adapters):
    working_adapters = adapters.copy()
    joltage = OUTLET_JOLTAGE
    deltas = []

    while len(working_adapters) > 0:
        qualifying_adapters = set(filter(lambda adapter_joltage: adapter_joltage - joltage <= MAX_JOLTAGE_DIFFERENCE, working_adapters))

        # always take the lowest joltage adapter, to ensure all adapters are used
        adapter = min(qualifying_adapters)

        working_adapters.remove(adapter)
        deltas.append(adapter - joltage)
        joltage = adapter
    
    # account for built in adapter joltage
    joltage += DEVICE_ADAPTER_JOLTAGE_ADJ
    deltas.append(DEVICE_ADAPTER_JOLTAGE_ADJ)

    return deltas.count(1) *  deltas.count(3)

def build_graph(all_adapters):
    graph = {}

    adapters = all_adapters.copy()
    adapters.insert(0, 0)

    for i, adapter in enumerate(adapters):
        remaining_adapters = adapters[i + 1:]
        if not graph.get(adapter):
            graph[adapter] = set(filter(lambda other_adapter: other_adapter - adapter <= MAX_JOLTAGE_DIFFERENCE, remaining_adapters))

    #print(adapters, graph)
    return graph

def count_paths(adapters):
    graph = build_graph(adapters)
    path_counts = {}
    
    graph_adapters = list(graph.keys())
    graph_adapters.sort()

    start = min(graph_adapters)

    for adapter in reversed(graph_adapters):
        adapter_options = graph[adapter]
        if not adapter_options:
            path_counts[adapter] = 1
        else:
            path_counts[adapter] = sum([path_counts[i] for i in adapter_options])
    
    return path_counts[start]

def run(label, file):
    adapters = read_input(file)
    adapters.sort()
    print("{} 1: {}".format(label, connect(adapters)))
    print("{} 2: {}".format(label, count_paths(adapters)))

run("test 1", TEST_INPUT_FILE_1)
run("test 2", TEST_INPUT_FILE_2)
run("test 3", TEST_INPUT_FILE_3)
run("part", INPUT_FILE)

'''
0 1 2 3 6
---------
0 1 2 3 6
0 1 3 6
0 2 3 6
0 3 6
'''