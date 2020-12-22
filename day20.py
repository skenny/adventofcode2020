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

    def is_corner(self):
        return len(self.neighbours) == 2

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

    def find_neighbour_edges(self):
        aaa = []
        for neighbour in self.neighbours:
            neighbour_edges = neighbour.edges()

            right = self.right_edge()
            if right in neighbour_edges or self.reverse_edge(right) in neighbour_edges:
                aaa.append("right")

            left = self.left_edge()
            if left in neighbour_edges or self.reverse_edge(left) in neighbour_edges:
                aaa.append("left")

            top = self.top_edge()
            if top in neighbour_edges or self.reverse_edge(top) in neighbour_edges:
                aaa.append("top")

            bottom = self.bottom_edge()
            if bottom in neighbour_edges or self.reverse_edge(bottom) in neighbour_edges:
                aaa.append("bottom")

        print("tile", self.id, "neighbour edges are", aaa)
        return aaa

    def flip_horizontal(self):
        self.rows = list(map(lambda row: self.reverse_edge(row), self.rows))

    def flip_vertical(self):
        self.rows = list(reversed(self.rows))

    def rotate(self, n):
        for i in range(n):
            new_rows = []
            for i in range(self.dimensions):
                row = ""
                for j in reversed(range(self.dimensions)):
                    row += self.rows[j][i]
                new_rows.append(row)
            self.rows = new_rows

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
    return list(filter(lambda tile: tile.is_corner(), tiles))

def arrange_tiles(tiles):
    dimensions = int(math.sqrt(len(tiles)))
    corners = find_corners(tiles)
    unplaced_tile_ids = list(map(lambda tile: tile.id, tiles))

    image = []
    for i in range(dimensions):
        image.append([None] * dimensions)

    # place a cornerstone
    cornerstone = corners[0]
    while True:
        neighbour_edges = cornerstone.find_neighbour_edges()
        if "right" in neighbour_edges and "bottom" in neighbour_edges:
            break
        if "right" in neighbour_edges and "top" in neighbour_edges:
            cornerstone.flip_vertical()
            break
        cornerstone.rotate(1)

    print("oriented correctly!")
    
    image[0][0] = cornerstone

    for y in range(0, dimensions):
        for x in range(0, dimensions):
            # skip the cornerstone
            if y == 0 and x == 0:
                continue

            prev_tile = image[y - 1][x] if x == 0 else image[y][x - 1]

            if x == 0:
                target_edge = prev_tile.bottom_edge()
                print("checking", x, y, prev_tile, target_edge)

                matching_tile = None
                for neighbour_tile in prev_tile.neighbours:
                    print("\tchecking neighbour", neighbour_tile)

                    if target_edge == neighbour_tile.top_edge():
                        print("\t\ttop, regular")
                        matching_tile = neighbour_tile
                        break
                    if target_edge == neighbour_tile.reverse_edge(neighbour_tile.top_edge()):
                        print("\t\ttop, reversed")
                        neighbour_tile.flip_horizontal()
                        matching_tile = neighbour_tile
                        break
                    if target_edge == neighbour_tile.right_edge():
                        print("\t\tright, regular")
                        neighbour_tile.rotate(3)
                        matching_tile = neighbour_tile
                        break
                    if target_edge == neighbour_tile.reverse_edge(neighbour_tile.right_edge()):
                        print("\t\tright, reversed")
                        neighbour_tile.flip_vertical()
                        neighbour_tile.rotate(3)
                        matching_tile = neighbour_tile
                        break
                    if target_edge == neighbour_tile.bottom_edge():
                        print("\t\tbottom, regular")
                        neighbour_tile.flip_vertical()
                        matching_tile = neighbour_tile
                        break
                    if target_edge == neighbour_tile.reverse_edge(neighbour_tile.bottom_edge()):
                        print("\t\tbottom, reversed")
                        # aka rotate(2)
                        neighbour_tile.flip_vertical()
                        neighbour_tile.flip_horizontal()
                        matching_tile = neighbour_tile
                        break
                    if target_edge == neighbour_tile.left_edge():
                        print("\t\tleft, regular")
                        neighbour_tile.flip_vertical()
                        neighbour_tile.rotate(1)
                        matching_tile = neighbour_tile
                        break
                    if target_edge == neighbour_tile.reverse_edge(neighbour_tile.left_edge()):
                        print("\t\tleft, reversed")
                        neighbour_tile.rotate(1)
                        matching_tile = neighbour_tile
                        break

                print("\tfound match", matching_tile)
            else:
                target_edge = prev_tile.right_edge()
                print("checking", x, y, prev_tile, target_edge)

                matching_tile = None
                for neighbour_tile in prev_tile.neighbours:
                    print("\tchecking neighbour", neighbour_tile)

                    if target_edge == neighbour_tile.top_edge():
                        print("\t\ttop, regular")
                        neighbour_tile.flip_horizontal()
                        neighbour_tile.rotate(3)
                        matching_tile = neighbour_tile
                        break
                    if target_edge == neighbour_tile.reverse_edge(neighbour_tile.top_edge()):
                        print("\t\ttop, reversed")
                        neighbour_tile.rotate(3)
                        matching_tile = neighbour_tile
                        break
                    if target_edge == neighbour_tile.right_edge():
                        print("\t\tright, regular")
                        neighbour_tile.flip_horizontal()
                        matching_tile = neighbour_tile
                        break
                    if target_edge == neighbour_tile.reverse_edge(neighbour_tile.right_edge()):
                        print("\t\tright, reversed")
                        neighbour_tile.flip_vertical()
                        neighbour_tile.flip_horizontal()
                        matching_tile = neighbour_tile
                        break
                    if target_edge == neighbour_tile.bottom_edge():
                        print("\t\tbottom, regular")
                        neighbour_tile.rotate(1)
                        matching_tile = neighbour_tile
                        break
                    if target_edge == neighbour_tile.reverse_edge(neighbour_tile.bottom_edge()):
                        print("\t\tbottom, reversed")
                        neighbour_tile.flip_vertical()
                        neighbour_tile.rotate(1)
                        matching_tile = neighbour_tile
                        break
                    if target_edge == neighbour_tile.left_edge():
                        print("\t\tleft, regular")
                        matching_tile = neighbour_tile
                        break
                    if target_edge == neighbour_tile.reverse_edge(neighbour_tile.left_edge()):
                        print("\t\tleft, reversed")
                        neighbour_tile.flip_vertical()
                        matching_tile = neighbour_tile
                        break

                print("\tfound match", matching_tile)

            image[y][x] = matching_tile
        print(image)
    # TODO

def run(label, input_file):
    tiles = read_input(input_file)
    test_fit_tiles(tiles)

    print("{} 1: {}".format(label, reduce(lambda total, tile: total * tile.id, find_corners(tiles), 1)))
    arrange_tiles(tiles)

run("test", "day20-input-test")
#run("part", "day20-input")
