from ancestry import Ancestry
from typing import Dict
import helper
from char_class import Class


class Character:
    def __init__(self, a_class: Class, a_ancestry: Ancestry):
        self.a_class = a_class
        self.ancestry = a_ancestry
        self.name: str = ""
        self.abilities: Dict = {}
        self.hit_points: int = 0
        self.level: int = 1
        self.initiative: int = 0
        self.load: int = 0
        self.resilience: int = 0
        self.retainers: int = 0
        self.magic_items: int = 0
        self.supply: int = 0

    def set_name(self, name: str):
        self.name = name

    def generate(self, name: str = ""):
        self.name = name
        self.abilities = helper.generate_abilities(self.ancestry.roll_table)
        self.hit_points = self.a_class.starting_hp + self.abilities['CON']['mod']
        full_equipment = self.a_class.equipments + helper.get_sundries(self.a_class.sundries_roll)
        self.a_class.equipments = full_equipment
        self.load = self.abilities['STR']['score']
        self.resilience = self.abilities['CON']['score']
        self.initiative = self.abilities['DEX']['score']
        self.retainers = self.abilities['CHA']['score']
        self.supply = self.abilities['INT']['score']
        self.magic_items = 1 if self.abilities['CHA']['mod'] < 1 else self.abilities['CHA']['mod']
