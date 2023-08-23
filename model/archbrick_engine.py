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
    def __init__(self, hex_start, hex_end, river_type):
        self.hex_start = hex_start
        self.hex_end = hex_end
        self.river_type = river_type


class ArchbrickEngine:
    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width
        self.hex_flower = {}
        self.icon_def = 'include https://campaignwiki.org/contrib/gnomeyland.txt'
        self.grid = {}
        self.ocean_sides = None
        self.land_sides = None
        self.rivers: [RiverSpec] = []

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
        self._step_10_init_river(grid_map)

        # final formatting for text-mapper
        for col in grid_map:
            for hex in col:
                text_mapper = text_mapper + f'{hex.col + 1:02}{hex.row + 1:02} {hex.terrain.value} \"h= {hex.terrain_height} qrs:{hex.q}.{hex.r}.{hex.s}\"' + '\n'

        return text_mapper + self.icon_def

    def _step_1_init_map(self, grid_map):

        def offset_to_cube(hex: Hex):
            q = hex.col
            r = hex.row - (hex.col - (hex.col & 1)) / 2
            hex.q = int(q)
            hex.r = int(r)
            hex.s = int(-q - r)

        h = range(0, self.height)
        w = range(0, self.width)
        for col in w:
            for row in h:
                current_hex = Hex(col=col, row=row)
                current_hex.text_mapper = f'{col + 1:02}{row + 1:02} {current_hex.terrain.value}'
                grid_map[col, row] = current_hex
                offset_to_cube(current_hex)

    def _step_2_ocean(self, grid_map):
        nb_side = dice.roll("1d6").pop() - 2
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
        self._extend_ocean_ocean(grid_map, sides_with_ocean, 1, -2, 3)

    def _step_4_extend_secondary_ocean(self, grid_map, sides_with_ocean):
        print('step4')
        self._extend_ocean_ocean(grid_map, sides_with_ocean, 2, -3, 2)

    def _step_5_place_mountains(self, grid_map):
        print('step5')
        nb_mountains = sum(dice.roll(f'{round(self.height * self.width / 100)}d6'))
        print(f'there are {nb_mountains} mountains')
        for mountain in range(0, nb_mountains):
            a_hex = grid_map[dice.roll(f'1d{self.width}').pop() - 1, dice.roll(f'1d{self.height}').pop() - 1]
            while a_hex.terrain in [TerrainType.ocean, TerrainType.big_mountain]:
                a_hex = grid_map[dice.roll(f'1d{self.width}').pop() - 1, dice.roll(f'1d{self.height}').pop() - 1]
            a_hex.terrain = TerrainType.big_mountain

    def _step_6_extend_mountains(self, grid_map: np.ndarray):
        print('step6')
        self._extend_moutains(grid_map, TerrainType.big_mountain, TerrainType.mountain, 4)

    def _step_7_extend_mountains(self, grid_map: np.ndarray):
        print('step7')
        self._extend_moutains(grid_map, TerrainType.mountain, TerrainType.mountain2, 2)

    def _step_8_extend_mountains(self, grid_map: np.ndarray):
        print('step8')
        for col in grid_map:
            for hex in col:
                if hex.terrain == TerrainType.mountain:
                    hex.terrain = TerrainType.big_mountain

        self._extend_moutains(grid_map, TerrainType.big_mountain, TerrainType.hill, 6)

    def _step_9_extend_hills(self, grid_map: np.ndarray):
        print('step9')
        for col in grid_map:
            for hex in col:
                hex.is_done = False

        for col in grid_map:
            for hex in col:
                if hex.terrain != TerrainType.plain_grass: continue
                self._chance_to_be_if_near(grid_map, hex, TerrainType.hill, TerrainType.hill2, 3)

    def _step_10_init_river(self, grid_map: np.ndarray):
        print('step10')
        nb_of_rolls = round(self.height * self.width / 100)
        rivers = []

        for roll in range(0, nb_of_rolls):
            roll = dice.roll("1d6").pop()
            if roll == 1:
                continue
            if roll in [2, 3, 4]:
                a_river = RiverSpec(hex_start=None, hex_end=None, river_type=RiverType.normal)
                rivers.append(a_river)
            if roll == 5:
                a_river = RiverSpec(hex_start=None, hex_end=None, river_type=RiverType.normal)
                b_river = RiverSpec(hex_start=None, hex_end=None, river_type=RiverType.normal)
                rivers.append(a_river)
                rivers.append(b_river)
            if roll == 6:
                a_river = RiverSpec(hex_start=None, hex_end=None, river_type=RiverType.joining_two)
                rivers.append(a_river)
        print('rivers:', rivers)

        self.land_sides = np.setdiff1d([1, 2, 3, 4], self.ocean_sides)
        for river in rivers:
            self._define_river_specs(river, grid_map)

        # set terrain height
        for col in grid_map:
            for hex in col:
                if hex.terrain == TerrainType.ocean:
                    hex.terrain_height = 0
                    continue
                if hex.terrain in [TerrainType.hill, TerrainType.hill2]:
                    hex.terrain_height = 2
                    continue
                if hex.terrain in [TerrainType.big_mountain, TerrainType.mountain, TerrainType.mountain2]:
                    hex.terrain_height = 3
                    continue
                hex.terrain_height = 1
        print('stop')

    def _chance_to_be_if_near(self, grid_map, hex: Hex, near_terrain: TerrainType, to_be_terrain: TerrainType,
                              x_chance: int, else_terrain: TerrainType = None):
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

        def is_out_of_bounds(col: int, row: int):
            if col < 0 or col >= self.width:
                return True
            if row < 0 or row >= self.height:
                return True
            return False

        def is_even_col(col: int):
            return (col % 2) == 0

        def check_one_near_hex(hex: Hex, gridmap, col_offset: int, row_offset: int, terrain_type: TerrainType):
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

    def _define_river_specs(self, river: RiverSpec, grid_map):
        if len(self.land_sides) > 0:
            if self._x_chance_in_6(3):
                river.hex_start = self._get_random_hex_of_type([TerrainType.big_mountain], grid_map)
            else:
                river.hex_start = self._get_random_hex_from_edge(grid_map, self.land_sides)
        else:
            river.hex_start = self._get_random_hex_of_type([TerrainType.big_mountain], grid_map)

        if len(self.ocean_sides) > 0:
            river.hex_end = self._get_random_hex_from_edge(grid_map, self.ocean_sides)
        else:
            river.hex_end = self._get_random_hex_from_edge(grid_map, self.land_sides)

    def _get_random_hex_of_type(self, terrains: [TerrainType], grid_map):
        a_hex = grid_map[dice.roll(f'1d{self.width}').pop() - 1, dice.roll(f'1d{self.height}').pop() - 1]
        while a_hex.terrain in terrains:
            a_hex = grid_map[dice.roll(f'1d{self.width}').pop() - 1, dice.roll(f'1d{self.height}').pop() - 1]
        return a_hex

    def _get_random_hex_from_edge(self, grid_map, sides: []):
        side = random.choice(sides)
        if side == 1:
            return random.choice(grid_map[:, 0])
        if side == 3:
            return random.choice(grid_map[:, -1])
        if side == 2:
            return random.choice(grid_map[-1, :])
        if side == 4:
            return random.choice(grid_map[0, :])
