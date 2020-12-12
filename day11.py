import math

INPUT_FILE = "day11-input"
TEST_INPUT_FILE = "day11-input-test"

OCCUPIED = "#"
EMPTY = "L"

def read_input(file):
    with open(file, "r") as fin:
        return [list(l.strip()) for l in fin.readlines()]

def fill_seats(grid, seat_counter):
    #print_grid(grid)

    new_grid = []
    num_seats_changed = 0

    for i, row in enumerate(grid):
        new_row = []
        for j, col in enumerate(row):
            occupied_adjacent = seat_counter(grid, i, j) #count_occupied_adjacent_seats(grid, i, j)
            if col == EMPTY and occupied_adjacent == 0:
                new_row.append(OCCUPIED)
                num_seats_changed += 1
            elif col == OCCUPIED and occupied_adjacent >= 4:
                new_row.append(EMPTY)
                num_seats_changed += 1
            else:
                new_row.append(col)
        new_grid.append(new_row)

    #print_grid(new_grid)
    return (new_grid, num_seats_changed)

def find_angle_between(x, y, x2, y2):
    return (360 - ((math.atan2(y - y2, x2 - x) * 180 / math.pi) - 90)) % 360

def count_occupied_seats(grid):
    return sum(list(map(lambda row: row.count(OCCUPIED), grid)))

def count_occupied_adjacent_seats(grid, row, col):
    num_rows = len(grid)
    num_cols = len(grid[0])
    offsets = range(-1, 2)

    adjacent_seats = []
    for i in offsets:
        r = row + i
        for j in offsets:
            c = col + j
            if not (i == 0 and j == 0) and 0 <= r < num_rows and 0 <= c < num_cols:
                adjacent_seats.append(grid[r][c])
    
    return adjacent_seats.count(OCCUPIED)

def count_occupied_in_sight_seats(grid, row, col):
    return 0

def print_grid(grid):
    [print("".join(r)) for r in grid]
    print("-" * len(grid[0]))

def adjust_seating(grid, seat_counter):
    working_grid = [row.copy() for row in grid]
    while True:
        new_grid, num_seats_changed = fill_seats(working_grid, seat_counter)
        if num_seats_changed == 0:
            break
        working_grid = new_grid
    return count_occupied_seats(working_grid)

def run(label, input_file):
    grid = read_input(input_file)
    print("{} 1: {}".format(label, adjust_seating(grid, count_occupied_adjacent_seats)))
    print("{} 2: {}".format(label, adjust_seating(grid, count_occupied_in_sight_seats)))

run("test", TEST_INPUT_FILE)
#run("part", INPUT_FILE)