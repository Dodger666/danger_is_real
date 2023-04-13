from typing import Dict

import dice
import random
from model.ose_char_class import cleric, dwarf, elf, hobbit, fighter, thief, magicuser
from model.ose_equipment import get_equipment

syllables = [
    "A",
    "Ael",
    "Af",
    "Ak",
    "Al",
    "Am",
    "An",
    "Ar",
    "Baf",
    "Bar",
    "Bee",
    "Bel",
    "Ber",
    "Berd",
    "Bes",
    "Bo",
    "Bo",
    "Bol",
    "Bor",
    "Bran",
    "Brose",
    "Bru",
    "Bur",
    "Car",
    "Chor",
    "Cig",
    "Cla",
    "Da",
    "Da",
    "Dan",
    "Do",
    "Do",
    "Dock",
    "Doh",
    "Don",
    "Dor",
    "Dor",
    "Dre",
    "Drebb",
    "E",
    "Eg",
    "Ek",
    "El",
    "El",
    "End",
    "Er",
    "Er",
    "Es",
    "Eth",
    "Eth",
    "Ev",
    "Fal",
    "Fan",
    "Far",
    "Feg",
    "Fen",
    "Fi",
    "Ful",
    "Fum",
    "Ga",
    "Gahn",
    "Gaith",
    "Gar",
    "Gar",
    "Gen",
    "Ger",
    "Glen",
    "Go",
    "Go",
    "Gram",
    "Grink",
    "Gulf",
    "Ha",
    "Hag",
    "Hal",
    "Han",
    "Harg",
    "Ho",
    "Hol",
    "Hor",
    "I",
    "Ig",
    "In",
    "Ith",
    "Jax",
    "Jo",
    "Jur",
    "Ka",
    "Kan",
    "Kra",
    "Krac",
    "Ky",
    "La",
    "Laf",
    "Lag",
    "Lap",
    "Le",
    "Lef",
    "Lem",
    "Lis", "Lo",
    "Lu",
    "Mal",
    "Mar",
    "Me",
    "Mer",
    "Mez",
    "Mez",
    "Mich",
    "Mil",
    "Mis",
    "Mo",
    "Mo",
    "Moo",
    "Mul",
    "Mun",
    "Mun",
    "Mur",
    "Mus",
    "Na",
    "Na",
    "Ned",
    "Nes",
    "Nick",
    "No",
    "Nor",
    "Nos",
    "Nu",
    "O",
    "Omes",
    "Os",
    "Pal",
    "Pen",
    "Phil",
    "Po",
    "Pos",
    "Poy",
    "Pres",
    "Pus",
    "Quas",
    "Que",
    "Ra",
    "Rag",
    "Ralt",
    "Ram",
    "Ray",
    "Ree",
    "Rem",
    "Rin",
    "Ris",
    "Ro",
    "Ro",
    "Ron",
    "Sa",
    "Sa",
    "See",
    "Ser",
    "Shal",
    "Sho",
    "Sho",
    "Sil",
    "Sit",
    "Spor",
    "Sun",
    "Sur",
    "Sus",
    "Tar",
    "Tar",
    "Tas",
    "Tee",
    "Ten",
    "Ten",
    "Teth",
    "To",
    "To",
    "Ton",
    "Ton",
    "Tra",
    "Treb",
    "Tred",
    "Tue",
    "U",
    "Va",
    "Vak",
    "Ven",
    "Ver",
    "Wal",
    "Web",
    "Wil",
    "Xor",
    "Y",
    "Yor",
    "Ys",
    "Zef",
    "Zell",
    "Zen",
    "Zer",
    "Zo",
    "Zo",
    "Zort"]


def get_mu_spell(character: Dict):
    if character['class'] == 'Magic-User':
        spells = ['Charm Person', 'Sleep']
        return spells[int(dice.roll('1d2')) - 1]
    return ""


def get_hp(character):
    while True:
        hp = int(dice.roll(character['dv']))
        if hp > 2:
            break;

    hp += int(character['conb'])
    if hp == 0:
        hp = 1
    return hp


def get_alignment():
    alignment = ['Loyal', 'Chaotique', 'Neutre']
    return alignment[int(dice.roll('1d3')) - 1]


def get_ac(character: Dict):
    ac = 10
    if 'leather' in character['armor']:
        ac += 2
    if 'chain' in character['armor']:
        ac += 4
    if 'plate' in character['armor']:
        ac += 6

    shield = next((item for item in character['gear'] if 'shield' in item), None)
    if shield:
        ac += 1
    ac += int(character['dexb'])
    return ac


def get_xp_bonus(character: Dict):

    if character['classe'] == 'Elfe':
        if character['int'] >= 16 and character['int'] >= 13:
            return '+10%'
        if character['int'] >= 13 and character['int'] >= 13:
            return '+5%'
        return '0%'

    if character['classe'] == 'Hobbit':
        if character['dex'] >= 13 and character['for'] >= 13:
            return '+10%'
        if character['dex'] >= 13 or character['for'] >= 13:
            return '+5%'
        return '0%'

    prime_score = character[character['prime']]

    if prime_score >= 16:
        return '+10%'
    if prime_score >= 13:
        return '+5%'
    if prime_score >= 9:
        return '0%'
    if prime_score >= 6:
        return '-10%'
    if prime_score >= 3:
        return '-20%'

    return '-3'


def get_class(character: Dict):
    abi = {'for': character["for"], 'dex': character["dex"], 'int': character["int"], 'sag': character["sag"]}
    abi_sorted = dict(sorted(abi.items(), key=lambda item: item[1], reverse=True))
    best = list(abi_sorted.keys())[0]

    if best == 'for': return random.choice([dwarf, fighter, hobbit, elf])
    if best == 'dex': return random.choice([thief, hobbit])
    if best == 'int': return random.choice([magicuser, elf])
    if best == 'sag': return cleric

    return random.choice([cleric, magicuser, elf, hobbit, fighter, thief, dwarf])



def get_ability_bonus(score):

    if score >= 18:
        return '+3'
    if score >= 16:
        return '+2'
    if score >= 13:
        return '+1'
    if score >= 9:
        return '0'
    if score >= 6:
        return '-1'
    if score >= 4:
        return '-2'

    return '-3'


def get_cha_bonus(score):
    if score >= 18:
        return '+2'
    if score >= 16:
        return '+1'
    if score >= 13:
        return '+1'
    if score >= 9:
        return '0'
    if score >= 6:
        return '-1'
    if score >= 4:
        return '-1'

    return '-2'


def _get_syllable():
    return syllables[int(dice.roll('1d100')) - 1] if int(dice.roll('1d2')) == 1 else syllables[
        int(dice.roll('1d100')) + 99]


def get_name():
    nb_syl = sum(dice.roll('1d100'))
    if nb_syl <= 10:
        return str(_get_syllable()).capitalize()
    if nb_syl <= 70:
        return str(_get_syllable() + _get_syllable()).capitalize()
    if nb_syl <= 90:
        return str(_get_syllable() + _get_syllable() + _get_syllable()).capitalize()

    return str(_get_syllable() + _get_syllable() + _get_syllable() + _get_syllable()).capitalize()

def get_ac(has_shield, armor, dex_bonus):
    armor = armor.strip()
    acnu = ac = 10 + int(dex_bonus)

    if has_shield:
        ac += 1
    if armor == 'armure de cuir':
        ac += 2
    if armor == 'cotte de mailles':
        ac += 4
    if armor == 'armure de plaques':
        ac += 2
    return ac, acnu


def get_movement(armor):
    armor = armor.strip()
    if armor == 'armure de cuir':
        return '9m', '27m', '27km'
    if armor == 'cotte de mailles' or armor == 'armure de plaques':
        return '6m', '18m', '18km'

    return '12m', '36m', '36km'



# noinspection PyDictCreation
def generate_char():
    character = {'pj': get_name(),
                 'titre': '',
                 'al': get_alignment(),
                 'niv': '1',
                 'pv': '',
                 'pvmax': '',
                 'init': '',
                 'mvren': '',
                 'mvext': '',
                 'mvvoy': '',
                 'ca': '',
                 'canu': '',
                 'bonusatt': '',
                 'bonusdist': '',
                 'for': sum(dice.roll('3d6')),
                 'int': sum(dice.roll('3d6')),
                 'sag': sum(dice.roll('3d6')),
                 'dex': sum(dice.roll('3d6')),
                 'con': sum(dice.roll('3d6')),
                 'cha': sum(dice.roll('3d6')),
                 'forb': '',
                 'intb': '',
                 'sagb': '',
                 'dexb': '',
                 'conb': '',
                 'chab': '',
                 'xp': '0',
                 'pp': '',
                 'po': '',
                 'pe': '',
                 'pa': '',
                 'pc': ''}

    character.update(get_class(character))

    character['bonusatt'] = character['forb'] = get_ability_bonus(character['for'])
    character['intb'] = get_ability_bonus(character['int'])
    character['sagb'] = get_ability_bonus(character['sag'])
    character['bonusdist'] = character['dexb'] = get_ability_bonus(character['dex'])
    character['conb'] = get_ability_bonus(character['con'])
    character['chab'] = get_cha_bonus(character['cha'])

    character['pv'] = character['pvmax'] = get_hp(character)
    character['xpbonus'] = get_xp_bonus(character)
    eq_list, has_shield, armor, po = get_equipment(character['classe'])
    character['po'] = po
    character['equip1'] = '\n'.join(eq_list[:5])
    character['equip2'] = '\n'.join(eq_list[5:-1])
    character['ca'], character['canu'] = get_ac(has_shield, armor, character['dexb'])
    character['mvren'], character['mvext'], character['mvvoy'] = get_movement(armor)

    return character
