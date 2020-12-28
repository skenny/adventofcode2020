class TileFloor:

    def __init__(self):
        self.tiles = dict()

    def flip_tile(self, path):
        x = 0
        y = 0
        for direction in path:
            if direction == "ne":
                x += 1
                y += 1
            if direction == "e":
                x += 2
            if direction == "se":
                x += 1
                y -= 1
            if direction == "nw":
                x -= 1
                y += 1
            if direction == "w":
                x -= 2
            if direction == "sw":
                x -= 1
                y -= 1

        coord = (x, y)
        current_color = self.tiles.get(coord, False)
        self.tiles[coord] = not current_color

    def count_black_tiles(self):
        return sum([1 if tile else 0 for tile in self.tiles.values()])

def read_input(file):
    with open(file, "r") as fin:
        instrs = []
        for line in fin.readlines():
            instr = []
            instr_chars = list(line.strip())
            while len(instr_chars) > 0:
                c = instr_chars.pop(0)
                if c == "s" or c == "n":
                    c += instr_chars.pop(0)
                instr.append(c)
            instrs.append(instr)
        return instrs

def run(label, input_file):
    instrs = read_input(input_file)
    print("{} 1: {}".format(label, flip_tiles(instrs)))

def flip_tiles(instructions):
    tile_floor = TileFloor()
    for instr in instructions:
        tile_floor.flip_tile(instr)
    return tile_floor.count_black_tiles()

run("test", "day24-input-test")
run("part", "day24-input")