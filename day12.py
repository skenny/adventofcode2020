INPUT_FILE = "day12-input"
TEST_INPUT_FILE = "day12-input-test"

def read_input(file):
    with open(file, "r") as fin:
        return [l.strip() for l in fin.readlines()]

def navigate(steps):
    # E is 0, S is 90, W is 180, N is 270
    direction = 0
    x = 0
    y = 0

    for step in steps:
        action = step[0]
        units = int(step[1:])

        if action == "F":
            if direction == 0:
                action = "E"
            if direction == 90:
                action = "S"
            if direction == 180:
                action = "W"
            if direction == 270:
                action = "N"

        if action == "N": y += units
        if action == "S": y -= units
        if action == "E": x += units
        if action == "W": x -= units
        if action == "L": direction = (direction - units) % 360
        if action == "R": direction = (direction + units) % 360

    return abs(x) + abs(y)

def run(label, input_file):
    steps = read_input(input_file)
    print("{} 1: {}".format(label, navigate(steps)))

run("test", TEST_INPUT_FILE)
run("part", INPUT_FILE)