from typing import List
from helper import Ability


class Class:
    def __init__(self):
        self.starting_hp: int = 0
        self.sundries_roll: int = 0
        self.equipments: List = []


class Warrior(Class):
    def __init__(self):
        self.name = "Warrior"
        self.starting_hp = 6
        self.hit_dice = "1d10"
        self.armor_allowed = "all"
        self.weapons_proficient = "all"
        self.abilities_proficient = [Ability.STR.name, Ability.CON.name]
        self.checks_proficient = "Coordination, tactics, will, archetype"
        self.equipments = ["Armor of your choice",
                           "Shield",
                           "2 one handed weapons",
                           "1 two handed weapon",
                           "Smith’s kit (1 load, 2 SUP to refill)",
                           "Healer’s kit (1 load, 2 SUP to refill)",
                           "rations"]
        self.sundries_roll = 3
        self.spellcasting = "None"


class Zealot(Class):
    def __init__(self):
        self.name = "Zealot"
        self.starting_hp = 5
        self.hit_dice = "1d8"
        self.armor_allowed = "all"
        self.weapons_proficient = "simple"
        self.abilities_proficient = [Ability.WIS.name, Ability.CHA.name]
        self.checks_proficient = "Spellcasting, history, insight, archetype"
        self.equipments = ["Armor of your choice",
                           "Shield",
                           "1 one handed simple weapons",
                           "Holy symbol",
                           "Healer’s kit (1 load, 2 SUP to refill)",
                           "rations"]
        self.sundries_roll = 2
        self.spellcasting = "3 cantrips, 1 divine spell (level1)"


class Mage(Class):
    def __init__(self):
        self.name = "Mage"
        self.starting_hp = 4
        self.hit_dice = "1d6"
        self.armor_allowed = "Shields"
        self.weapons_proficient = "simple"
        self.abilities_proficient = [Ability.CON.name, Ability.INT.name]
        self.checks_proficient = "Spellcasting, finesse, negotiation, archetype"
        self.equipments = ["Potionery glassware",
                           "Shield or hunting bow",
                           "1 one handed simple weapons",
                           "Scribe’s kit (0 load, 5 SUP to refill)",
                           "Spell components (3 levels, 6 SUP)",
                           "rations"]
        self.sundries_roll = 1
        self.spellcasting = "3 cantrips, 1 arcane spell (level1)"
        self.spellcasting = "None"


class Thief(Class):
    def __init__(self):
        self.name = "Thief"
        self.starting_hp = 4
        self.hit_dice = "1d6"
        self.armor_allowed = "light, shield"
        self.weapons_proficient = "all"
        self.abilities_proficient = [Ability.DEX.name, Ability.INT.name]
        self.checks_proficient = "Stealth, deception, senses, tools, archetype"
        self.equipments = ["Light armor",
                           "2 one handed weapons",
                           "1 ranged weapon",
                           "ammunition",
                           "1 use poison(0 load, 2 SUP to refill)",
                           "Thief’s kit (1 load, 5 SUP to refill)",
                           "rations"]
        self.sundries_roll = 5
        self.spellcasting = "None"


class ElfParagon(Class):
    def __init__(self):
        self.name = "Elf paragon"
        self.starting_hp = 4
        self.hit_dice = "1d6"
        self.armor_allowed = "light, shield"
        self.weapons_proficient = "simple, war bow"
        self.abilities_proficient = [Ability.STR.name, Ability.INT.name]
        self.checks_proficient = "Stealth, senses, arcane, archetype"
        self.equipments = ["Light armor",
                           "Shield",
                           "1 simple one handed weapons",
                           "war bow",
                           "arrows",
                           "Elf token",
                           "Elf Healer’s kit (1 load, 2 SUP to refill)",
                           "rations"
                           ]
        self.sundries_roll = 3
        self.spellcasting = "None"


class HalflingParagon(Class):
    def __init__(self):
        self.name = "Halfling paragon"
        self.starting_hp = 5
        self.hit_dice = "1d8"
        self.armor_allowed = "light, shield"
        self.weapons_proficient = "simple"
        self.abilities_proficient = [Ability.DEX.name, Ability.CHA.name]
        self.checks_proficient = "Stealth, haggling, will- power, archetype"
        self.equipments = ["Light armor",
                           "Shield",
                           "2 simple weapons",
                           "Halfling token",
                           "Healer’s kit (1 load, 2 SUP to refill)",
                           "Halfling chef’s kit (1 load)",
                           "rations"
                           ]
        self.sundries_roll = 5
        self.spellcasting = "None"


class DwarfParagon(Class):
    def __init__(self):
        self.name = "Dwarf paragon"
        self.starting_hp = 6
        self.hit_dice = "1d10"
        self.armor_allowed = "all"
        self.weapons_proficient = "all"
        self.abilities_proficient = [Ability.CON.name, Ability.WIS.name]
        self.checks_proficient = "Mountain, athletics, diplomacy, archetype"
        self.equipments = ["Armor of your choice",
                           "3 weapons",
                           "Dungoneer’s kit",
                           "Dwarf Smith’s kit (1 load, 2 SUP to refill)",
                           "dwarf token",
                           "rations"
                           ]
        self.sundries_roll = 4
        self.spellcasting = "None"
