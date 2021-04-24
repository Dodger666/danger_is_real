import math
from collections import namedtuple
from enum import Enum
from typing import Dict
import dice


class Ability(Enum):
    STR = "STR",
    CON = "CON",
    DEX = "DEX",
    INT = "INT",
    WIS = "WIS",
    CHA = "CHA",


def generate_abilities(roll_table: Dict):
    AbilityValues = namedtuple('AbilityValues', 'score mod')
    result = {
            Ability.STR.name: None,
            Ability.CON.name: None,
            Ability.DEX.name: None,
            Ability.INT.name: None,
            Ability.WIS.name: None,
            Ability.CHA.name: None
        }
    for key, val in roll_table.items():
        score = sum(dice.roll(val))
        mod = math.floor((score - 10) / 2) if score > 1 else -4
        result[key.name] = AbilityValues(score, mod)
    return result


def get_sundries(nb: int):
    table = {
        1: "30m rope",
        2: "3m iron chain",
        3: "iron manacles",
        4: "lantern",
        5: "sac of marbles",
        6: "3m Oilskin tarp",
        7: "small barrel",
        8: "iron crawbar",
        9: "hammer, chisel",
        10: "15m bandages",
        11: "coarse rasp",
        12: "10m copper wire",
        13: "noisemaker, auto",
        14: "thread, needle",
        15: "folding shovel",
        16: "glass lens",
        17: "steel mirror",
        18: "fishing net",
        19: "threaded sinew",
        20: "roll of raw wool",
    }
    return [table[dice.roll('1d20')[0]] for r in range(1, nb + 1)]

