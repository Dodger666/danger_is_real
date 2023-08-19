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
        sides_with_ocean = self._step_2_ocean(grid_map)
        self._step_3_extend_ocean(grid_map, sides_with_ocean)
        self._step_4_extend_secondary_ocean(grid_map, sides_with_ocean)

        # final formatting for text-mapper
        for col in grid_map:
            for hex in col:
                text_mapper = text_mapper + f'{hex.col + 1:02}{hex.row + 1:02} {hex.terrain.value}' + '\n'

        return text_mapper + self.icon_def

    def _step_1_init_map(self, grid_map):
        h = range(0, self.height)
        w = range(0, self.width)
        for col in w:
            for row in h:
                current_hex = Hex(col=col, row=row)
                current_hex.text_mapper = f'{col + 1:02}{row + 1:02} {current_hex.terrain.value}'
                grid_map[col, row] = current_hex

    def _step_2_ocean(self, grid_map):
        nb_side = dice.roll("1d6").pop()-2
        if nb_side < 1:
            return
        sides_has_ocean = random.sample(range(1, 5), nb_side)
        print('shore sides:', sides_has_ocean)
        for side in sides_has_ocean:
            if side == 1:
                for hex in grid_map[:, 0]:
                    hex.terrain = TerrainType.ocean
            if side == 3:
                for hex in grid_map[:, -1]:
                    hex.terrain = TerrainType.ocean
            if side == 2:
                for hex in grid_map[-1, :]:
                    hex.terrain = TerrainType.ocean
            if side == 4:
                for hex in grid_map[0, :]:
                    hex.terrain = TerrainType.ocean
        return sides_has_ocean

    def _step_3_extend_ocean(self, grid_map, sides_with_ocean):
        print('step3')
        self._extend_ocean_ocean(grid_map, sides_with_ocean,1, -2, 3)

    def _step_4_extend_secondary_ocean(self, grid_map, sides_with_ocean):
        print('step4')
        self._extend_ocean_ocean(grid_map, sides_with_ocean, 2, -3, 2)

    def chance_to_be(self, grid_map, hex: Hex, terrain: TerrainType, x_chance: int):
        if self._is_near(hex, terrain, grid_map) and self._x_chance_in_6(x_chance) and not hex.is_done:
            hex.terrain = terrain
            print(f"hex:{hex.col + 1},{hex.row + 1} is ocean")
        hex.is_done = True

    def _is_near(self, hex: Hex, terrain_type: TerrainType, gridmap):

        def is_out_of_bounds(col: int, row:int):
            if col < 0 or col >= self.width:
                return True
            if row < 0 or row >= self.height:
                return True
            return False

        def is_even_col(col: int):
            return (col % 2) == 0

        def check_one_near_hex(hex: Hex, gridmap, col_offset:int, row_offset:int, terrain_type: TerrainType):
            if not is_out_of_bounds(hex.col + col_offset, hex.row + row_offset):
                hex_to_check: Hex = gridmap[hex.col + col_offset, hex.row + row_offset]
                if hex_to_check.terrain == terrain_type:
                    print(
                        f'hex {hex.col + 1},{hex.row + 1} is near hex {hex_to_check.col + 1},{hex_to_check.row + 1},{hex_to_check.terrain.value}')
                    return True

        # North
        row_offset = -1
        col_offset = 0
        if check_one_near_hex(hex, gridmap, col_offset, row_offset, terrain_type):
            return True

        # N-E
        row_offset = -1 if is_even_col(hex.col) else 0
        col_offset = 1
        if check_one_near_hex(hex, gridmap, col_offset, row_offset, terrain_type):
            return True

        # S-E
        row_offset = 0 if is_even_col(hex.col) else 1
        col_offset = 1
        if check_one_near_hex(hex, gridmap, col_offset, row_offset, terrain_type):
            return True

        # South
        row_offset = 1
        col_offset = 0
        if check_one_near_hex(hex, gridmap, col_offset, row_offset, terrain_type):
            return True

        # S-W
        row_offset = 0 if is_even_col(hex.col) else +1
        col_offset = -1
        if check_one_near_hex(hex, gridmap, col_offset, row_offset, terrain_type):
            return True
        # N-W
        row_offset = -1 if is_even_col(hex.col) else 0
        col_offset = -1
        if check_one_near_hex(hex, gridmap, col_offset, row_offset, terrain_type):
            return True

        return False

    def _x_chance_in_6(self, x_chance: int):
        return dice.roll("1d6").pop() <= x_chance

    def _extend_ocean_ocean(self, grid_map, sides_with_ocean, index_1: int, index_2: int, chance: int):
        print('step4')
        if not sides_with_ocean:
            return
        if 1 in sides_with_ocean:
            for hex in grid_map[:, index_1]:
                self.chance_to_be(grid_map, hex, TerrainType.ocean, chance)
        if 3 in sides_with_ocean:
            for hex in grid_map[:, index_2]:
                self.chance_to_be(grid_map, hex, TerrainType.ocean, chance)
        if 2 in sides_with_ocean:
            for hex in grid_map[index_2, :]:
                self.chance_to_be(grid_map, hex, TerrainType.ocean, chance)
        if 4 in sides_with_ocean:
            for hex in grid_map[index_1, :]:
                self.chance_to_be(grid_map, hex, TerrainType.ocean, chance)






