from enum import Enum
import random
import dice
import numpy as np


class TerrainType(str, Enum):
    plain_grass = "light-green grass",
    plain_dry = "plain_dry",
    hill = "green hill",
    hill2 = "green hill",
    hill_forest = "forest-hill",
    big_mountain = "rock mountains",
    mountain = "rock mountain",
    mountain2 = "rock mountain",
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
        self.ocean_sides = None

    def generate_map(self):

        grid_map = np.ndarray(shape=(self.width, self.height), dtype=Hex)
        text_mapper = ""
        self._step_1_init_map(grid_map)
        sides_with_ocean = self._step_2_ocean(grid_map)
        self._step_3_extend_ocean(grid_map, sides_with_ocean)
        self._step_4_extend_secondary_ocean(grid_map, sides_with_ocean)
        self._step_5_place_mountains(grid_map)
        self._step_6_extend_mountains(grid_map)
        self._step_7_extend_mountains(grid_map)
        self._step_8_extend_mountains(grid_map)
        self._step_9_extend_hills(grid_map)

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
        self.ocean_sides = sides_has_ocean
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

    def _step_5_place_mountains(self, grid_map):
        nb_mountains = sum(dice.roll(f'{round(self.height*self.width / 100)}d6'))
        print(f'there are {nb_mountains} mountains')
        for mountain in range(0, nb_mountains):
            a_hex = grid_map[dice.roll(f'1d{self.width}').pop()-1, dice.roll(f'1d{self.height}').pop()-1]
            while a_hex.terrain in [TerrainType.ocean, TerrainType.big_mountain]:
                a_hex = grid_map[dice.roll(f'1d{self.width}').pop()-1, dice.roll(f'1d{self.height}').pop()-1]
            a_hex.terrain = TerrainType.big_mountain

    def _step_6_extend_mountains(self, grid_map: np.ndarray):
        self._extend_moutains(grid_map, TerrainType.big_mountain, TerrainType.mountain, 4)

    def _step_7_extend_mountains(self, grid_map: np.ndarray):
        self._extend_moutains(grid_map, TerrainType.mountain, TerrainType.mountain2, 2)

    def _step_8_extend_mountains(self, grid_map: np.ndarray):
        for col in grid_map:
            for hex in col:
                if hex.terrain == TerrainType.mountain:
                    hex.terrain = TerrainType.big_mountain

        self._extend_moutains(grid_map, TerrainType.big_mountain, TerrainType.hill, 6)

    def _step_9_extend_hills(self, grid_map: np.ndarray):
        for col in grid_map:
            for hex in col:
                hex.is_done = False

        for col in grid_map:
            for hex in col:
                if hex.terrain != TerrainType.plain_grass: continue
                self._chance_to_be_if_near(grid_map, hex, TerrainType.hill, TerrainType.hill2, 3)



    def _chance_to_be_if_near(self, grid_map, hex: Hex, near_terrain: TerrainType, to_be_terrain: TerrainType, x_chance: int, else_terrain: TerrainType = None):
        if self._is_near(hex, near_terrain, grid_map) and not hex.is_done:
            if self._x_chance_in_6(x_chance):
                hex.terrain = to_be_terrain
                print(f"hex:{hex.col + 1},{hex.row + 1} is {to_be_terrain}")
            else:
                if else_terrain:
                    hex.terrain = else_terrain
                    print(f"hex:{hex.col + 1},{hex.row + 1} is {else_terrain}")
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
                self._chance_to_be_if_near(grid_map, hex, TerrainType.ocean, TerrainType.ocean, chance)
        if 3 in sides_with_ocean:
            for hex in grid_map[:, index_2]:
                self._chance_to_be_if_near(grid_map, hex, TerrainType.ocean, TerrainType.ocean, chance)
        if 2 in sides_with_ocean:
            for hex in grid_map[index_2, :]:
                self._chance_to_be_if_near(grid_map, hex, TerrainType.ocean, TerrainType.ocean, chance)
        if 4 in sides_with_ocean:
            for hex in grid_map[index_1, :]:
                self._chance_to_be_if_near(grid_map, hex, TerrainType.ocean, TerrainType.ocean, chance)

    def _extend_moutains(self, grid_map, terrain_near: TerrainType, terrain_to_be: TerrainType, chance: int):
        for col in grid_map:
            for hex in col:
                hex.is_done = False

        for col in grid_map:
            for hex in col:
                if hex.terrain != TerrainType.plain_grass: continue
                self._chance_to_be_if_near(grid_map, hex, terrain_near, terrain_to_be, chance, TerrainType.hill)






