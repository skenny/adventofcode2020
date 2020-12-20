class Tile:

    def __init__(self, id, rows):
        self.id = id
        self.rows = rows

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

    def connects_with(self, other_tile):
        other_edges = other_tile.edges()
        for edge in self.edges():
            if edge in other_edges or self.reverse_edge(edge) in other_edges:
                return True
        return False

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

def find_corner_tiles(tiles):
    tile_counts = {}
    for target_tile in tiles:
        tile_counts[target_tile.id] = 0
        for test_tile in tiles:
            if target_tile.id == test_tile.id:
                continue
            if target_tile.connects_with(test_tile):
                tile_counts[target_tile.id] = tile_counts[target_tile.id] + 1
    corner_tiles = []
    prod = 1
    for tile_id, connect_count in tile_counts.items():
        if connect_count == 2:
            corner_tiles.append(tile_id)
            prod *= tile_id
    return prod

def run(label, input_file):
    tiles = read_input(input_file)
    print("{} 1: {}".format(label, find_corner_tiles(tiles)))

run("test", "day20-input-test")
run("part", "day20-input")