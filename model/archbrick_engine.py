from enum import Enum
from typing import Dict, List
import random
import dice
import numpy as np


class TerrainType(str, Enum):
    plain_grass = "light-green grass",
    plain_dry = "plain_dry",
    hill = "hill",
    hill_forest = "hill_forest",
    mountain = "mountain",
    mountain_forest = "mountain_forest",
    ocean = "ocean",
    swamp = "swamp",
    forest = "forest"


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


class ArchbrickEngine:
    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width
        self.hex_flower = {}
        self.icon_def = 'include https://campaignwiki.org/contrib/gnomeyland.txt'
        self.grid = {}

    def generate_map(self):

        grid_map = np.ndarray(shape=(self.width, self.height), dtype=Hex)
        text_mapper = ""
        self._step_1_init_map(grid_map)
        self._step_2_ocean(grid_map)
        self._step_3_extend_ocean(grid_map)

        # final formating for text-mapper
        for col in grid_map:
            for hex in col:
                text_mapper = text_mapper + f'{hex.col + 1:02}{hex.row + 1:02} {hex.terrain.value}' + '\n'

        return text_mapper + self.icon_def

    def _step_1_init_map(self, grid_map):
        h = range(0, self.height)
        w = range(0, self.width)
        for col in w:
            # grid_map = np.append(grid_map, [])
            for row in h:
                current_hex = Hex(col=col, row=row)
                current_hex.text_mapper = f'{col + 1:02}{row + 1:02} {current_hex.terrain.value}'
                # grid_map = np.append(grid_map[col], current_hex)
                grid_map[col, row] = current_hex

    def _step_2_ocean(self, grid_map):
        nb_side = dice.roll("1d6").pop()-2
        if nb_side < 1:
            return
        sides_has_ocean = random.sample(range(1, 5), nb_side)
        print('shore sides:', sides_has_ocean)
        for side in sides_has_ocean:
            if side == 1:
                for col in grid_map:
                    col[0].terrain = TerrainType.ocean
            if side == 3:
                for col in grid_map:
                    col[-1].terrain = TerrainType.ocean
            if side == 2:
                for row in grid_map[-1]:
                    row.terrain = TerrainType.ocean
            if side == 4:
                for row in grid_map[0]:
                    row.terrain = TerrainType.ocean

    def _step_3_extend_ocean(self, grid_map):
        for col in grid_map[1:-2]:
            for hex in col[1:-2]:
                if self._is_near(hex, TerrainType.ocean, grid_map) and (dice.roll("1d6").pop() <= 3) and not hex.is_done:
                    hex.terrain = TerrainType.ocean
                    print(f"hex:{hex.col},{hex.row} is ocean")
                hex.is_done = True

    def _is_near(self, hex: Hex, terrain_type: TerrainType, gridmap):
        try:
            if gridmap[hex.col][hex.row-1].terrain == terrain_type:
                return True
        except:
            pass
        try:
            if gridmap[hex.col+1][hex.row - 1].terrain == terrain_type:
                return True
        except:
            pass
        try:
            if gridmap[hex.col+1][hex.row].terrain == terrain_type:
                return True
        except:
            pass
        try:
            if gridmap[hex.col][hex.row + 1].terrain == terrain_type:
                return True
        except:
            pass
        try:
            if gridmap[hex.col - 1][hex.row + 1].terrain == terrain_type:
                return True
        except:
            pass
        try:
            if gridmap[hex.col - 1][hex.row - 1].terrain == terrain_type:
                return True
        except:
            pass
        return False






