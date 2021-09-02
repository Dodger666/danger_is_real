from typing import Dict, List
import random
import dice


class Hex:

    def __init__(self, content_text: str, index: int, directions: Dict):
        self.index = index
        # key is direction: 1 is up 4 is down // value is hex index, if several values, pick one
        self.directions = directions
        self.content_text = content_text


class HexFlowerEngine:
    def __init__(self, hex_flower: List[Hex], icon_def: str):
        self.icon_def = icon_def
        self.hex_flower = {}
        for a_hex in hex_flower:
            self.hex_flower[a_hex.index] = a_hex

    def generate_map(self, width: int, height: int, start_hex: int):
        h = range(1, height + 1)
        w = range(1, width + 1)
        grid_map = {}
        text_mapper = ""
        current_hex = self.hex_flower[start_hex]
        for c in h:
            grid_map[c] = {}
            for r in w:
                direction = self._get_direction()
                current_hex = self.hex_flower[random.choice(current_hex.directions[direction])]
                output = f'{c:02}{r:02} {random.choice(current_hex.content_text)}'
                grid_map[c][r] = output
                text_mapper = text_mapper + output + '\n'
                # print(output)
                # print(direction,current_hex.index, output)
        return text_mapper + self.icon_def

    def _get_direction(self):
        roll = sum(dice.roll('2d6'))
        navigation_hex = {
            2: 2,
            3: 2,
            4: 3,
            5: 3,
            6: 4,
            7: 4,
            8: 5,
            9: 5,
            10: 6,
            11: 6,
            12: 1
        }
        return navigation_hex[roll]


terrains = \
    {'icon_def': 'include https://campaignwiki.org/contrib/gnomeyland.txt',
     'hexes':
         [
             Hex(content_text=['light-green grass'], index=1,
                 directions={1: [5], 2: [3], 3: [4], 4: [1, 2, 3], 5: [6], 6: [2]}),
             Hex(content_text=['light-green grass'], index=2,
                 directions={1: [7], 2: [5], 3: [1], 4: [17], 5: [11], 6: [4]}),
             Hex(content_text=['light-green grass'], index=3,
                 directions={1: [8], 2: [6], 3: [9], 4: [18], 5: [1], 6: [5]}),
             Hex(content_text=['dust grass'], index=4, directions={1: [9], 2: [7], 3: [2], 4: [14], 5: [16], 6: [1]}),
             Hex(content_text=['light-green grass'], index=5,
                 directions={1: [10], 2: [8], 3: [3], 4: [1], 5: [2], 6: [7]}),
             Hex(content_text=['light-green bush'], index=6,
                 directions={1: [11], 2: [1], 3: [14], 4: [16], 5: [3], 6: [8]}),
             Hex(content_text=['dust grass'], index=7, directions={1: [12], 2: [10], 3: [5], 4: [2], 5: [4], 6: [9]}),
             Hex(content_text=['light-green bush'], index=8,
                 directions={1: [13], 2: [11], 3: [6], 4: [3], 5: [5], 6: [10]}),
             Hex(content_text=['sand desert'], index=9, directions={1: [14], 2: [12], 3: [7], 4: [4], 5: [18], 6: [3]}),
             Hex(content_text=['dark-grey swamp', 'water'], index=10,
                 directions={1: [14], 2: [12], 3: [7], 4: [4], 5: [18], 6: [3]}),
             Hex(content_text=['green forest'], index=11,
                 directions={1: [16], 2: [2], 3: [17], 4: [6], 5: [8], 6: [13]}),
             Hex(content_text=['sand desert'], index=12,
                 directions={1: [17], 2: [15], 3: [10], 4: [7], 5: [9], 6: [14]}),
             Hex(content_text=['green forest'], index=13,
                 directions={1: [18], 2: [16], 3: [11], 4: [8], 5: [10], 6: [15]}),
             Hex(content_text=['dust hill'], index=14, directions={1: [4], 2: [17], 3: [12], 4: [9], 5: [19], 6: [4]}),
             Hex(content_text=['light-grey hill'], index=15,
                 directions={1: [19], 2: [18], 3: [13], 4: [10], 5: [12], 6: [17]}),
             Hex(content_text=['light-grey forest-hill'], index=16,
                 directions={1: [6], 2: [4], 3: [19], 4: [11], 5: [13], 6: [18]}),
             Hex(content_text=['light-grey hill'], index=17,
                 directions={1: [2], 2: [19], 3: [15], 4: [12], 5: [14], 6: [11]}),
             Hex(content_text=['light-grey hill'], index=18,
                 directions={1: [3], 2: [9], 3: [16], 4: [13], 5: [15], 6: [19]}),
             Hex(content_text=['grey mountains'], index=19,
                 directions={1: [19], 2: [19], 3: [18], 4: [15], 5: [17], 6: [19]})]
     }

primal = \
    {'icon_def': 'include https://campaignwiki.org/contrib/default.txt',
     'hexes':
    [
    Hex(content_text=['hill'], index=1,
        directions={1: [5], 2: [3], 3: [4], 4: [1, 2, 3], 5: [6], 6: [2]}),
    Hex(content_text=['mountain'], index=2, directions={1: [7], 2: [5], 3: [1], 4: [17], 5: [11], 6: [4]}),
    Hex(content_text=['mountain'], index=3, directions={1: [8], 2: [6], 3: [9], 4: [18], 5: [1], 6: [5]}),
    Hex(content_text=['mountain'], index=4, directions={1: [9], 2: [7], 3: [2], 4: [14], 5: [16], 6: [1]}),
    Hex(content_text=['hill'], index=5, directions={1: [10], 2: [8], 3: [3], 4: [1], 5: [2], 6: [7]}),
    Hex(content_text=['mountain'], index=6, directions={1: [11], 2: [1], 3: [14], 4: [16], 5: [3], 6: [8]}),
    Hex(content_text=['jungle'], index=7, directions={1: [12], 2: [10], 3: [5], 4: [2], 5: [4], 6: [9]}),
    Hex(content_text=['jungle'], index=8, directions={1: [13], 2: [11], 3: [6], 4: [3], 5: [5], 6: [10]}),
    Hex(content_text=['hill'], index=9, directions={1: [14], 2: [12], 3: [7], 4: [4], 5: [18], 6: [3]}),
    Hex(content_text=['swamp', 'wetland', 'tower', 'sea', 'house', 'pyramid'], index=10,
        directions={1: [14], 2: [12], 3: [7], 4: [4], 5: [18], 6: [3]}),
    Hex(content_text=['hill'], index=11, directions={1: [16], 2: [2], 3: [17], 4: [6], 5: [8], 6: [13]}),
    Hex(content_text=['jungle'], index=12, directions={1: [17], 2: [15], 3: [10], 4: [7], 5: [9], 6: [14]}),
    Hex(content_text=['jungle'], index=13, directions={1: [18], 2: [16], 3: [11], 4: [8], 5: [10], 6: [15]}),
    Hex(content_text=['mountain'], index=14, directions={1: [4], 2: [17], 3: [12], 4: [9], 5: [19], 6: [4]}),
    Hex(content_text=['hill'], index=15,
        directions={1: [19], 2: [18], 3: [13], 4: [10], 5: [12], 6: [17]}),
    Hex(content_text=['mountain'], index=16,
        directions={1: [6], 2: [4], 3: [19], 4: [11], 5: [13], 6: [18]}),
    Hex(content_text=['mountain'], index=17,
        directions={1: [2], 2: [19], 3: [15], 4: [12], 5: [14], 6: [11]}),
    Hex(content_text=['mountain'], index=18,
        directions={1: [3], 2: [9], 3: [16], 4: [13], 5: [15], 6: [19]}),
    Hex(content_text=['volcano'], index=19,
        directions={1: [1], 2: [14], 3: [18], 4: [15], 5: [17], 6: [16]})]
     }
