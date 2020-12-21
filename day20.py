class Tile:

    def __init__(self, id, rows):
        self.id = id
        self.rows = rows
        self.neighbours = set()

    def edges(self):
        edges = []
        
        # top edge
        edges.append(self.rows[0])

        # bottom edge
        edges.append(self.rows[-1])

        # left edge
        edges.append("".join(list(map(lambda row: row[0], self.rows))))

        # right edge
        edges.append("".join(list(map(lambda row: row[-1], self.rows))))
        
        return edges

    def reverse_edge(self, edge):
        return edge[::-1]

    def test_fit(self, other_tile):
        other_edges = other_tile.edges()
        for edge in self.edges():
            if edge in other_edges or self.reverse_edge(edge) in other_edges:
                self.neighbours.add(other_tile)

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

def run(label, input_file):
    tiles = read_input(input_file)
    test_fit_tiles(tiles)

    corner_product = 1
    for tile in tiles:
        if len(tile.neighbours) == 2:
            corner_product *= tile.id

    print("{} 1: {}".format(label, corner_product))

run("test", "day20-input-test")
run("part", "day20-input")