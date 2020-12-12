INPUT_FILE = "day11-input"
TEST_INPUT_FILE = "day11-input-test"

OCCUPIED = "#"
EMPTY = "L"

def read_input(file):
    with open(file, "r") as fin:
        return [list(l.strip()) for l in fin.readlines()]

def fill_seats(grid):
    print_grid(grid)

    new_grid = []
    num_seats_changed = 0

    for i, row in enumerate(grid):
        new_row = []
        for j, col in enumerate(row):
            occupied_adjacent = count_occupied_adjacent_seats(grid, i, j)
            if col == EMPTY and occupied_adjacent == 0:
                new_row.append(OCCUPIED)
                num_seats_changed += 1
            elif col == OCCUPIED and occupied_adjacent >= 4:
                new_row.append(EMPTY)
                num_seats_changed += 1
            else:
                new_row.append(col)
        new_grid.append(new_row)

    print_grid(new_grid)
    return (new_grid, num_seats_changed)

def count_occupied_seats(grid):
    return sum(list(map(lambda row: row.count(OCCUPIED), grid)))

def count_occupied_adjacent_seats(grid, row_num, col_num):
    row = grid[row_num]
    num_rows = len(grid)
    num_cols = len(row)

    adjacent_seats = []

    # previous row
    if row_num > 0:
        prev_row = grid[row_num - 1]
        if col_num > 0:
            adjacent_seats.append(prev_row[col_num - 1])
        adjacent_seats.append(prev_row[col_num])
        if col_num < num_cols - 1:
            adjacent_seats.append(prev_row[col_num + 1])

    # current row
    if col_num > 0:
        adjacent_seats.append(row[col_num - 1])
    if col_num < num_cols - 1:
        adjacent_seats.append(row[col_num + 1])

    # next row
    if row_num < num_rows - 1:
        next_row = grid[row_num + 1]
        if col_num > 0:
            adjacent_seats.append(next_row[col_num - 1])
        adjacent_seats.append(next_row[col_num])
        if col_num < num_cols - 1:
            adjacent_seats.append(next_row[col_num + 1])

    return adjacent_seats.count(OCCUPIED)

def print_grid(grid):
    #[print("".join(r)) for r in grid]
    #print("-----")
    pass

def part1(grid):
    # TODO copy grid
    while True:
        new_grid, num_seats_changed = fill_seats(grid)
        if num_seats_changed == 0:
            break
        grid = new_grid
    return count_occupied_seats(grid)

def run(label, input_file):
    grid = read_input(input_file)
    print("{} 1: {}".format(label, part1(grid)))

run("test", TEST_INPUT_FILE)
run("part", INPUT_FILE)