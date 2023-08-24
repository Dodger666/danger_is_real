from enum import Enum


class TerrainType(str, Enum):
    plain_grass = "light-green grass",
    plain_dry = "plain_dry",
    hill = "green hill",
    hill2 = "green hill",
    hill_forest = "forest-hill",
    big_mountain = "rock mountains",
    mountain = "rock mountains",
    mountain2 = "rock mountains",
    mountain_forest = "mountain_forest",
    ocean = "ocean",
    swamp = "swamp",
    forest = "forest"


class RiverType(str, Enum):
    normal = "normal",
    joining_two = "joining_two"


class Hex:
    def __init__(self, col: int, row: int, terrain: TerrainType = TerrainType.plain_grass, is_dry: bool = False,
                 has_river: bool = False, is_done: bool = False):
        self.is_done = is_done
        self.has_river = has_river
        self.is_dry = is_dry
        self.terrain = terrain
        self.col = col
        self.row = row
        self.text_mapper = None
        self.q = 0
        self.r = 0
        self.s = 0
        self.g = 0
        self.h = 0

        self.terrain_height = int(1)
        self.adj_hexes = []

    def f(self):
        return self.g + self.h


class RiverSpec:
    def __init__(self, hex_start: Hex, hex_end: Hex, river_type: RiverType):
        self.hex_start = hex_start
        self.hex_end = hex_end
        self.river_type = river_type
        self.text_mapper = "None"
    def __repr__(self):
        return f'start {self.hex_start.col+1:02}{self.hex_start.row+1:02} end {self.hex_end.col+1:02}{self.hex_end.row+1:02} type {self.river_type} text {self.text_mapper}'
