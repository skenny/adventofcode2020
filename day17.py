import copy

INPUT_FILE = "day17-input"
TEST_INPUT_FILE = "day17-input-test"

ACTIVE = "#"
INACTIVE = "."

class PocketDimension:
    cubes = {}
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    min_z = 0
    max_z = 0

    def setup_grid(self, grid):
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                self.update_cube(x, y, 0, col)

    def get_cube(self, x, y, z):
        return self.cubes.get((x, y, z), INACTIVE)

    def activate_cube(self, x, y, z):
        self.update_cube(x, y, z, ACTIVE)

    def deactivate_cube(self, x, y, z):
        self.update_cube(x, y, z, INACTIVE)

    def update_cube(self, x, y, z, state):
        self.cubes[(x, y, z)] = state
        if x > self.max_x: self.max_x = x
        if x < self.min_x: self.min_x = x
        if y > self.max_y: self.max_y = y
        if y < self.min_y: self.min_y = y
        if z > self.max_z: self.max_z = z
        if z < self.min_z: self.min_z = z

    def count_active_neighbours(self, x, y, z):
        offsets = (-1, 0, 1)
        neighbours = []
        for xo in offsets:
            for yo in offsets:
                for zo in offsets:
                    if not (xo == 0 and yo == 0 and zo == 0):
                        neighbours.append(self.get_cube(x + xo, y + yo, z + zo))
        return neighbours.count(ACTIVE)

    def count_active_cubes(self):
        num_active = 0
        for k, v in self.cubes.items():
            num_active += 1 if v == ACTIVE else 0
        return num_active

    def make_copy(self):
        copy_version = PocketDimension()
        copy_version.cubes = copy.deepcopy(self.cubes)
        copy_version.min_x = self.min_x
        copy_version.max_x = self.max_x
        copy_version.min_y = self.min_y
        copy_version.max_y = self.max_y
        copy_version.min_z = self.min_z
        copy_version.max_z = self.max_z
        return copy_version

    def print(self):
        for z in range(self.min_z, self.max_z + 1):
            grid = []
            for y in range(self.min_y, self.max_y + 1):
                row = ""
                for x in range(self.min_x, self.max_x + 1):
                    row += self.get_cube(x, y, z)
                grid.append(row)
            print("z={}:\n{}\n{}".format(z, "\n".join(grid), "=" * len(grid[0])))

def read_input(file):
    with open(file, "r") as fin:
        return [l.strip() for l in fin]

def run(label, input_file):
    pocket_dimension = PocketDimension()
    pocket_dimension.setup_grid(read_input(input_file))
    
    for cycle in range(6):
        #print("cycle", cycle + 1)
        #pocket_dimension.print()

        new_pocket_dimension = pocket_dimension.make_copy()

        for x in range(pocket_dimension.min_x - 1, pocket_dimension.max_x + 2):
            for y in range(pocket_dimension.min_y - 1, pocket_dimension.max_y + 2):
                for z in range(pocket_dimension.min_z - 1, pocket_dimension.max_z + 2):
                    cube = pocket_dimension.get_cube(x, y, z)
                    num_active_neighbours = pocket_dimension.count_active_neighbours(x, y, z)
                    if cube == ACTIVE and num_active_neighbours not in (2, 3):
                        new_pocket_dimension.deactivate_cube(x, y, z)
                    if cube == INACTIVE and num_active_neighbours == 3:
                        new_pocket_dimension.activate_cube(x, y, z)
                        
        pocket_dimension = new_pocket_dimension

    print("{} 1: {}".format(label, pocket_dimension.count_active_cubes()))

run("test", TEST_INPUT_FILE)
#run("part", INPUT_FILE)