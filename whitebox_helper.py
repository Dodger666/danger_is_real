from typing import Dict

import dice

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
title = ["from Above",
         "from Afar",
         "from Below",
         "the Adept",
         "the Albino",
         "the Antiquarian",
         "the Arcane",
         "the Archaic",
         "the Barbarian",
         "the Batrachian",
         "the Battler",
         "the Bilious",
         "the Bold",
         "the Brave",
         "the Civilized",
         "the Collector",
         "the Cryptic",
         "the Curious",
         "the Dandy",
         "the Daring",
         "the Decadent",
         "the Delver",
         "the Distant",
         "the Eldritch",
         "the Exotic",
         "the Explorer",
         "the Fair",
         "the Fearless",
         "the Fickle",
         "the Foul",
         "the Furtive",
         "the Gambler",
         "the Ghastly",
         "the Gibbous",
         "the Great",
         "the Grizzled",
         "the Gruff",
         "the Bald",
         "the Haunted",
         "the Heavy",
         "the Hooded",
         "the Hunter",
         "the Imposing",
         "the Irreverent",
         "the Loathsome",
         "the Quiet",
         "the Lovely",
         "the Mantled",
         "the Veiled",
         "the Merciless",
         "the Mercurial",
         "the Mighty",
         "the Morose",
         "the Mutable",
         "the Mysterious",
         "the Obscure",
         "the Old/Young",
         "the Ominous",
         "the Peculiar",
         "the Perceptive",
         "the Pious",
         "the Quick",
         "the Ragged",
         "the Ready",
         "the Rough",
         "the Rugose",
         "the Scarred",
         "the Searcher",
         "the Shadowy",
         "the Short",
         "the Steady",
         "the Uncanny",
         "the Unexpected",
         "the Unknowable",
         "the Verbose",
         "the Vigorous",
         "the Wanderer",
         "the Wary",
         "the Weird",
         "the Ugly",
         "the First",
         "of the Red Cloak",
         "of the North",
         "of the Arid Wastes",
         "of the Beetling Brow",
         "of the Cyclopean City",
         "of the Dread Wilds",
         "of the Eerie Eyes",
         "of the Foetid Swamp",
         "of the Forgotten City",
         "of the Haunted Heath",
         "of the Hidden Valley",
         "of the Howling Hills",
         "of the Jagged Peaks",
         "of the Menacing Mien",
         "of the Savage Isle",
         "of the Tangled Woods",
         "of the Watchful Eyes",
         "of the South",
         "of the West"]
melee_weapons = [
                 "hand axe",
                 "mace",
                 "sword",
                 "battle axe", "2 battle axes"
                               "morning star",
                 "flail",
                 "warhammer",
                 "spear",
                 "halberd", "quarter-staff", "cudgel",
                 "two-handed sword","dagger", "2 daggers", "3 daggers"]
missile_weapons = ["short bow", "long bow", "dagger", "2 daggers", "3 daggers", "light crossbow", "heavy crossbow",
                   "sling"]

CLERIC = {
    'abilities': 'Use blunt weapons, only missile allowed is oil.<br>'
                 '+2 Save vs. poison and paralysis.<br>'
                 'Turn Undead: Use divine power to banish the undead.<br>',
    'gear': ["cudgel, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, wooden cross, 4 GP",
             "cudgel, shield, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, wooden cross, 4 GP",
             "mace, leather armor, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, wooden cross, 5 GP",
             "quarter-staff, leather armor, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, 12 iron spikes, wooden cross, 3 stakes & mallet, steel mirror, 10 GP"
             "chain armor, warhammer, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, wooden cross, 2 small sacks, 8 GP",
             "chain armor, shield, mace, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, wooden cross, 2 small sacks, 8 GP",
             "chain armor, shield, warhammer, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, wooden cross, 2 small sacks, 3 stakes & mallet, steel mirror, 10 GP",
             "plate armor, shield, mace, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, wooden cross, 10 GP",
             "plate armor, shield, warhammer, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 10′ pole, wooden cross, small sack, 2 GP",
             "plate armor, quarter-staff, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 50′ rope, silver cross, 4 GP",
             "cudgel, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, wooden cross, scroll, 4 GP",
             "plate armor, shield, mace, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 50′ rope, silver cross, 10 GP",
             "leather armor, mace, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, wooden cross, scroll, 2 flasks oil, 1 GP",
             "plate armor, shield, helmet, warhammer, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 50′ rope, silver cross, 3 stakes & mallet, steel mirror, 12 GP",
             "chain armor, warhammer, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, wooden cross, scroll, 10 GP",
             "plate armor, shield, helmet, mace, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 50′ rope, silver cross, vial holy water, 12 iron spikes, 3 stakes & mallet, small sack, 10 GP"]
}
FIGHTER = {
    'abilities': 'Fury: One attack per level per round against 1 HD or less foes.<br>'
                 '+2 Save vs. Death and Poison<br>',
    'gear': ["spear, dagger, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, 3 GP",
             "cudgel, leather armor, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, 1 GP",
             "leather armor, morning star, dagger, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, 3 GP",
             "leather armor, battle axe, hand axe, dagger, sling, pouch with 20 sling bullets, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, 7 GP",
             "chain armor, spear, dagger, sling, pouch with 20 sling bullets, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, 11 GP",
             "chain armor, shield, sword, dagger, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, 4 GP",
             "chain armor, spear, light crossbow, case with 30 quarrels, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, 11 GP",
             "plate armor, shield, sword, dagger, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, 4 GP",
             "plate armor, two-handed sword, 3 daggers, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, 2 flasks oil, 9 GP",
             "plate armor, shield, sword, light crossbow, case with 30 quarrels, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, 2 GP",
             "plate armor, flail, dagger, short bow, quiver of 20 arrows, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, small sack, 10 GP",
             "plate armor, shield, sword, light crossbow, case with 30 quarrels, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 10′ pole, 5 GP",
             "plate armor, helmet, 2 battle axes, dagger, light crossbow, case with 30 quarrels, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, 5 flasks oil, 15 GP",
             "plate armor, two-handed sword, dagger, short bow, quiver of 20 arrows, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 10′ pole, 2 small sacks, 15 GP",
             "plate armor, halberd, dagger, long bow, quiver of 20 arrows, 2 silver tipped arrows, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 50′ rope, 10 GP",
             "plate armor, shield, helmet, sword, 2 daggers, light crossbow, case with 30 quarrels, 4 silver tipped quarrels, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 10′ pole, 9 GP"]
}
MAGIC_USER = {
    'abilities': 'Use only daggers or staves, no armor allowed.<br>'
                 '+2 Save vs. spells, wands and staves.<br>',
    'gear': ["dagger, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, 4 GP",
             "2 daggers, 6 torches, backpack, waterskin, 1 week iron rations, 2 flasks oil, 50′ rope, 7 GP",
             "dagger, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 10′ pole, 7 GP",
             "dagger, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, vial of holy water, 9 GP",
             "dagger, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole 5 flasks of oil, silver mirror, belladona, 9 GP",
             "dagger, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, 2 vials holy water, 4 GP",
             "3 daggers, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 10′ pole, vial of holy water, 16 GP",
             "dagger, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, 2 vials holy water, 24 GP",
             "dagger, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 10′ pole, 67 GP",
             "dagger, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 50′ rope, 77 GP",
             "dagger, 6 torches, backpack, waterskin, 1 week iron rations, scroll, 10′ pole, 4 GP",
             "2 daggers, 6 torches, backpack, waterskin, 1 week iron rations, scroll, 50′ rope, 11 GP",
             "dagger, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, scroll, 10′ pole, 7 GP",
             "dagger, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, scroll, 50′ rope, 17 GP",
             "dagger, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, scroll, 10′ pole, 27 GP",
             "dagger, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, scroll, 50′ rope, 37 GP"]
}

THIEF = {
    'abilities': 'Back Stab: +2 To-Hit and double damage against unaware foes<br>'
                 '+2 Save vs. Traps (mundane or magic).<br>'
                 'Thievery: 2+6 chances in clandestine or stealth-based actions',
    'gear': [
        "cudgel, sling, pouch with 20 sling bullets, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, 4 GP",
        "cudgel, leather armor, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, 1 GP",
        "cudgel, dagger, sling, pouch with 20 sling bullets, leather armor, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, 6 GP",
        "sword, dagger, leather armor, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, 9 GP",
        "cudgel, light crossbow, case with 30 quarrels, leather armor, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, 6 GP",
        "sword, light crossbow, case of 30 quarrels, leather armor, 6 torches, backpack, waterskin, 1 week iron rations, 10′ pole, 7 GP",
        "sword, 2 daggers, 35 short bow, quiver of 20 arrows, leather armor, 6 torches, backpack, waterskin, 1 week iron rations, 50′ rope, 1 GP",
        "sword, dagger, leather armor, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 10′ pole, 32 GP",
        "sword, light crossbow, case of 30 quarrels, 2 silver tipped quarrels, leather armor, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 50′ rope, 10 GP",
        "sword, dagger, short bow, quiver of 20 arrows, leather armor, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 10′ pole, 17 GP",
        "sword, leather armor, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 50′ rope, 65 GP",
        "sword, light crossbow, case of 30 quarrels, 6 silver tipped quarrels, leather armor, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 10′ pole, 20 GP",
        "sword, short bow, quiver of 20 arrows, 6 silver tipped arrows, leather armor, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 50′ rope, 20 GP",
        "sword, 4 daggers, leather armor, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 10′ pole, 98 GP",
        "sword, light crossbow, case of 30 quarrels, leather armor, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 50′ rope, 80 GP",
        "sword, 3 daggers, short bow, quiver of 20 arrows, 8 silver tipped arrows, leather armor, backpack, waterskin, lantern, 4 flasks oil, 1 week iron rations, 10′ pole, 31 GP"]
}


def get_mu_spell(character: Dict):
    if character['class'] == 'Magic-User' or character['race'] == 'Elf':
        spells = ['Charm Person', 'Sleep']
        return spells[int(dice.roll('1d2')) - 1]
    return ""


def get_movement(character: Dict):
    return 9 if character['race'] in ["Dwarf", "Halfling"] else 12


def get_save(character: Dict):
    save = 14
    if character['class'] == 'Magic-User' or character['class'] == 'Cleric':
        save += 1
    return save


def get_hp(character: Dict):
    hp = int(dice.roll('1d6'))
    if character['class'] == 'Fighter' or character['race'] == 'Elf':
        hp += 1
    hp += int(character['conb'])
    if hp == 0:
        hp = 1
    return hp


def get_alignment(character):
    alignment = ['(Lawful)', '(Chaotic)', '(Neutral)']

    if character['class'] == 'Cleric':
        return alignment[int(dice.roll('1d2')) - 1]
    return alignment[int(dice.roll('1d3')) - 1]


def get_weapons(character: Dict):
    return next((item for item in character['gear'] if item.strip() in melee_weapons), ""), \
           next((item for item in character['gear'] if item.strip() in missile_weapons), "")


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


def split_gear_gold_armor(gear: str):
    list_gear = gear.split(',')
    gp = list_gear[-1]
    list_gear.pop()
    armor = next((item for item in list_gear if 'armor' in item), "")

    return list_gear, gp, armor


def get_gear(character: Dict):
    roll = int(dice.roll('3d6')) - 3
    if character['class'] == 'Cleric':
        gear, gold, ar = split_gear_gold_armor(CLERIC['gear'][roll])
        return gear, gold, ar, CLERIC['abilities']
    if character['class'] == 'Thief':
        gear, gold, ar = split_gear_gold_armor(THIEF['gear'][roll])
        return gear, gold, ar, THIEF['abilities']
    if character['class'] == 'Magic-User':
        gear, gold, ar = split_gear_gold_armor(MAGIC_USER['gear'][roll])
        return gear, gold, ar, MAGIC_USER['abilities']

    gear, gold, ar = split_gear_gold_armor(FIGHTER['gear'][roll])
    return gear, gold, ar, FIGHTER['abilities']


def get_xp_bonus(character: Dict):
    bonus = 5 if character['wis'] >= 15 else 0
    if character['race'] == 'Elf':
        if character['str'] >= 15 or character['int'] >= 15:
            return bonus + 5
    if character['class'] == 'Cleric' and character['wis'] >= 15:
        return bonus + 5
    if character['class'] == 'Fighter' and character['str'] >= 15:
        return bonus + 5
    if character['class'] == 'Thief' and character['dex'] >= 15:
        return bonus + 5
    if character['class'] == 'Magic-User' and character['int'] >= 15:
        return bonus + 5
    return bonus


def get_race():
    roll = int(dice.roll('1d20'))
    if roll <= 3:
        abilities = 'Giant-type creatures inflict half damage against you.<br>' \
                    '4-6 searching or 2-6 passively chances to spot traps, slanting passages,<br>and construction while underground.<br>' \
                    '+4 Save vs Magic.<br>' \
                    'Extra languages: gnomes, goblins, orcs, and kobolds.<br>'
        return "Dwarf", abilities
    if roll <= 6:
        abilities = '+1 To-Hit or Damage vs goblins, orcs, intelligent undead<br>and lycanthropes.<br>' \
                    'Immune to paralysis caused by undead.<br>' \
                    '4-6 searching or 2-6 passively chances to spot secrret doors<br>' \
                    'Extra languages: gnolls, goblins, orcs, and hobgoblins.<br>'
        return "Elf", abilities
    if roll <= 9:
        abilities = 'Giant-type creatures inflict half damage against you.<br>' \
                    '+2 To-Hit with missile weapons.<br>' \
                    '5-6 chances to hide or move silently out of combat.<br>' \
                    '+4 Save vs Magic.<br>' \
                    'Extra languages: see with Referee.<br>'
        return "Halfling", abilities
    return 'Human', ""


def get_class(character: Dict):
    abi = {'str': character["str"], 'dex': character["dex"], 'int': character["int"], 'wis': character["wis"]}
    abi_sorted = dict(sorted(abi.items(), key=lambda item: item[1], reverse=True))
    best = list(abi_sorted.keys())[0]
    # boost prime req to 10 if lower
    if character[best] < 10:
        character[best] = 10
    classes = ['Thief', 'Fighter', 'Cleric', 'Magic-User']

    if character['race'] == 'Elf':
        return 'Fighter<br>Magic-User'
    if character['race'] in ['Dwarf', 'Halfling']:
        if character["str"] > character["dex"]:
            return 'Fighter'
        if character["dex"] > character["str"]:
            return 'Thief'
        return classes[int(dice.roll('1d2')) - 1]
    if best == 'str': return 'Fighter'
    if best == 'dex': return 'Thief'
    if best == 'int': return 'Magic-User'
    if best == 'wis': return 'Cleric'
    return classes[int(dice.roll('1d4')) - 1]


def get_ability():
    score = sum(dice.roll('3d6'))
    bonus = 0
    if score >= 15:
        bonus = '+1'
    if score <= 6:
        bonus = '-1'
    return score, bonus


def get_syllable():
    return syllables[int(dice.roll('1d100')) - 1] if int(dice.roll('1d2')) == 1 else syllables[
        int(dice.roll('1d100')) + 99]


def get_name():
    nb_syl = sum(dice.roll('1d100'))
    if nb_syl <= 10:
        return str(get_syllable()).capitalize()
    if nb_syl <= 70:
        return str(get_syllable() + get_syllable()).capitalize()
    if nb_syl <= 90:
        return str(get_syllable() + get_syllable() + get_syllable()).capitalize()

    return str(get_syllable() + get_syllable() + get_syllable() + get_syllable()).capitalize()


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def chunk_gear(character):
    gear_chunks = chunks(character['gear'], 2)
    formatted_gear = ""
    for chunk in gear_chunks:
        formatted_gear += "&emsp;/&emsp;".join(chunk) + "<br>"
    return formatted_gear


def format_gear(character):
    if len(character['gear']) < 10:
        return "<br>".join(character['gear'])
    return chunk_gear(character)


# noinspection PyDictCreation
def generate_char():
    character = {}
    character["str"], character["strb"] = get_ability()
    character["dex"], character["dexb"] = get_ability()
    character["con"], character["conb"] = get_ability()
    character["int"], character["intb"] = get_ability()
    character["wis"], character["wisb"] = get_ability()
    character["cha"], character["chab"] = get_ability()

    character['race'], character['abilities'] = get_race()
    character['class'] = get_class(character)
    character['gear'], character['gp'], character['armor'], class_abilities = get_gear(character)
    character['abilities'] += '<br>' + class_abilities

    character["name"] = get_name() + " " + title[int(dice.roll('1d100')) - 1] + " " + get_alignment(character)
    character['lvl'] = '1'

    character['xp'] = f'({get_xp_bonus(character)}%)'
    character['ac'] = get_ac(character)
    character['wpn1'], character['wpn2'] = get_weapons(character)
    character['bhb'] = 0
    character['hp'] = get_hp(character)
    character['sv'] = get_save(character)
    character['mv'] = get_movement(character)
    character['spell'] = get_mu_spell(character)
    character['gear'] = format_gear(character)

    return character
