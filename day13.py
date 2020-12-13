import math

INPUT_FILE = "day13-input"
TEST_INPUT_FILE = "day13-input-test"

def read_input(file):
    with open(file, "r") as fin:
        return [l.strip() for l in fin.readlines()]

def find_best_train(earliest_departure_time, bus_ids):
    min_time_difference = 99
    departure_bus = None
    for bus_id in bus_ids:
        closest_departure_time = math.ceil(earliest_departure_time / bus_id) * bus_id
        time_difference = closest_departure_time - earliest_departure_time
        if time_difference < min_time_difference:
            min_time_difference = time_difference
            departure_bus = bus_id
    return departure_bus * min_time_difference

def run(label, input_file):
    input = read_input(input_file)
    earliest_departure_time = int(input[0])
    bus_ids = map(lambda i: int(i), filter(lambda i: i.isdigit(), input[1].split(",")))
    print("{} 1: {}".format(label, find_best_train(earliest_departure_time, bus_ids)))

run("test", TEST_INPUT_FILE)
run("part", INPUT_FILE)