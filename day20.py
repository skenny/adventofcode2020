import math
from functools import reduce

class Tile:

    def __init__(self, id, rows):
        self.id = id
        self.rows = rows
        self.dimensions = len(rows)
        self.top_neighbour = None
        self.right_neighbour = None
        self.bottom_neighbour = None
        self.left_neighbour = None
        self.neighbours = set()

    def __repr__(self):
        return str(self.id)

    def edges(self):
        return [self.top_edge(), self.right_edge(), self.bottom_edge(), self.left_edge()]

    def top_edge(self):
        return self.rows[0]

    def right_edge(self):
        return "".join(list(map(lambda row: row[-1], self.rows)))

    def bottom_edge(self):
        return self.rows[-1]

    def left_edge(self):
        return "".join(list(map(lambda row: row[0], self.rows)))

    def reverse_edge(self, edge):
        return edge[::-1]

    def test_fit(self, other_tile):
        other_edges = other_tile.edges()
        for edge in self.edges():
            if edge in other_edges or self.reverse_edge(edge) in other_edges:
                self.neighbours.add(other_tile)

    def flip_horizontal(self):
        self.rows = list(map(lambda row: self.reverse_edge(row), self.rows))

    def flip_vertical(self):
        self.rows = list(reversed(self.rows))

    def rotate(self, n):
        print("rotating", n)
        print("before rotate\n", "\n".join(self.rows))
        for i in range(n):
            new_rows = []
            for i in range(dimensions):
                row = ""
                for j in reversed(range(dimensions)):
                    row += self.rows[j][i]
                new_rows.append(row)
            self.rows = new_rows
        print("after rotate\n", "\n".join(self.rows))

def read_input(file):
    with open(file, "r") as fin:
        lines = [l.strip() for l in fin.readlines()]
        tile_id = None
        tile_rows = None
        tiles = []
        for line in lines:
            if len(line) == 0:
                continue
            if line.startswith("Tile "):
                if tile_id != None:
                    tiles.append(Tile(tile_id, tile_rows))
                tile_id = int(line[5:-1])
                tile_rows = []
                continue
            tile_rows.append(line)
        tiles.append(Tile(tile_id, tile_rows))
        return tiles

def test_fit_tiles(tiles):
    for target_tile in tiles:
        for test_tile in tiles:
            if not target_tile.id == test_tile.id:
                target_tile.test_fit(test_tile)

def find_corners(tiles):
    return list(filter(lambda tile: len(tile.neighbours) == 2, tiles))

def arrange_tiles(tiles):
    dimensions = int(math.sqrt(len(tiles)))
    corners = find_corners(tiles)
    unplaced_tile_ids = list(map(lambda tile: tile.id, tiles))

    map = []
    for i in range(dimensions):
        map.append([None] * dimensions)

    # place a cornerstone and adjacent tiles
    cornerstone = corners[0]
    cornerstone_neighbours = list(cornerstone.neighbours)
    map[0][0] = corners[0]
    map[0][1] = cornerstone_neighbours[0]
    map[1][0] = cornerstone_neighbours[1]
    unplaced_tile_ids.remove(cornerstone)
    unplaced_tile_ids.remove(cornerstone_neighbours[0])
    unplaced_tile_ids.remove(cornerstone_neighbours[1])

    for y in range(0, dimensions):
        for x in range(0, dimensions):
            # skip the cornerstone
            if y == 0 and x == 0:
                continue

            prev_tile = map[y - 1][x] if x == 0 else map[y][x - 1]

            map[y][x] = matching_tile
        print(map)
    # TODO

def run(label, input_file):
    tiles = read_input(input_file)
    test_fit_tiles(tiles)

    print("{} 1: {}".format(label, reduce(lambda total, tile: total * tile.id, find_corners(tiles), 1)))
    fit_tiles(tiles)

run("test", "day20-input-test")
#run("part", "day20-input")