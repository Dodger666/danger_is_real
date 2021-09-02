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
    def __init__(self, hex_flower: List[Hex]):
        self.hex_flower = {}
        for a_hex in hex_flower:
            self.hex_flower[a_hex.index] = a_hex

    def generate_map(self, width: int, height: int, start_hex: int):
        h = range(1, height)
        w = range(1, width)
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
        return text_mapper + 'include https://campaignwiki.org/contrib/gnomeyland.txt'

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