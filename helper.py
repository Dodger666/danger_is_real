import math
from enum import Enum
from io import BytesIO
from typing import Dict
import dice
import pdfrw


class Ability(str, Enum):
    STR = "STR",
    CON = "CON",
    DEX = "DEX",
    INT = "INT",
    WIS = "WIS",
    CHA = "CHA",


class ClassName(str, Enum):
    elf = "elf"
    dwarf = "dwarf"
    halfling = "halfling"
    warrior = "warrior"
    zealot = "zealot"
    mage = "mage"
    thief = "thief"


def generate_abilities(roll_table: Dict):
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
        result[key] = {'score': score, 'mod': mod}
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


def create_pdf(character):
    template_pdf = pdfrw.PdfReader('template.pdf')
    for annot in template_pdf.pages[0]['/Annots']:
        print(annot['/T'])
        map_annotation(annot, character)

    output = BytesIO()
    pdfrw.PdfWriter().write(
                output, template_pdf)
    return output


def map_annotation(annot, character):
    if annot['/T'] == '(Character Name)':
        annot.update(pdfrw.PdfDict(V=character.name))
    if annot['/T'] == '(Class)':
        annot.update(pdfrw.PdfDict(V=character.a_class.name))
    if annot['/T'] == '(Race)':
        annot.update(pdfrw.PdfDict(V=character.ancestry.race))
    if annot['/T'] == '(LVL)':
        annot.update(pdfrw.PdfDict(V=str(character.level)))
    if annot['/T'] == '(HP)':
        annot.update(pdfrw.PdfDict(V=str(character.hit_points)))
    if annot['/T'] == '(MAX)':
        annot.update(pdfrw.PdfDict(V=str(character.hit_points)))
    if annot['/T'] == '(Text22)':
        annot.update(pdfrw.PdfDict(V=str(character.abilities['STR']['score'])))



