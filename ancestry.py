from abc import ABC, abstractmethod
from typing import Dict

from helper import Ability


class Ancestry(ABC):
    def __init__(self):
        self.ancestry: Dict = {}
        self.roll_table: Dict = {}

    @abstractmethod
    def set_best_ability(self, best_ability: Ability):
        pass


class Halfling(Ancestry):
    def __init__(self):
        self.race: str = "Halfling"
        self.ancestry: Dict = {
            "GENERAL":
                "Unassuming, curious, eager. "
                "They wish to experience the world and revel in emotion.",
            "FEARLESS FRIENDS":
                "You empathize with and befriend anyone, bravely standing up for them against all odds."
                " Your comrades value your fellowship.",
            "SMALL BUT SUREFOOTED":
                "Gain dis/advantage to non-combat checks affected by size "
                "(+hiding, -lifting, +balance, -intimidation). If the GM is unsure, ignore."
        }
        self.roll_table: Dict = {
            Ability.STR: "5d6m3",
            Ability.CON: "5d6m3",
            Ability.DEX: "5d6m3",
            Ability.INT: "5d6m3",
            Ability.WIS: "4d6h3",
            Ability.CHA: "4d6h3",
        }

    def set_best_ability(self, best_ability: Ability):
        pass


class Dwarf(Ancestry):
    def __init__(self):
        self.race: str = "Dwarf"
        self.ancestry: Dict = {
            "GENERAL":
                "Productive, stubborn, hardy, patient. "
                "Care for legacy and monumental achievement.",
            "INDUSTRIOUS DELVERS":
                "You understand the fundamental scaffolds that loft the world. "
                "You can build and create nearly anything, but are always dissatisfied.",
            "SUBTERRANEAN SENSES":
                "You care little for the overworld. "
                "Increase all light levels by one step (well lit to brilliant). "
                "Stone sings to you but you fear open water."
        }
        self.roll_table: Dict = {
            Ability.STR: "4d6h3",
            Ability.CON: "4d6h3",
            Ability.DEX: "5d6m3",
            Ability.INT: "5d6m3",
            Ability.WIS: "5d6m3",
            Ability.CHA: "5d6m3",
        }

    def set_best_ability(self, best_ability: Ability):
        pass


class Elf(Ancestry):
    def __init__(self):
        self.race: str = "Elf"
        self.ancestry: Dict = {
            "GENERAL":
                "Cold, rational, regal, aloof, nearly immortal."
                " Elves care for introspection and perfection.",
            "APATHETIC ANCIENTS":
                "You’ve lived a dozen lifetimes; know a great deal, "
                "but may have become cynical."
                " You find it hard to empathize, but easy to recall.",
            "CHILDREN OF THE MOON":
                "You draw strength from the moon. Rest half as much in moonlight,"
                " but reduce your max RES by 1 per day you don’t see the moon."
        }
        self.roll_table: Dict = {
            Ability.STR: "5d6m3",
            Ability.CON: "5d6m3",
            Ability.DEX: "4d6h3",
            Ability.INT: "4d6h3",
            Ability.WIS: "5d6m3",
            Ability.CHA: "5d6m3",
        }

    def set_best_ability(self, best_ability: Ability):
        pass


class Human(Ancestry):
    def __init__(self):
        self.race: str = "Human"
        self.ancestry: Dict = {
            "GENERAL":
                "Passionate, creative, fervent, aspirational. Humanity is defined by its constant hunger.",
            "ZEALOUS OBSESSION":
                "You focus on your passions and pursue them endlessly. "
                "You learn quickly, and can master one niche subject to near deific levels.",
            "FOR THE CAUSE":
                "You can choose to bring yourself to 0 HP from extreme effort"
                " or self-sacrifice to pass any check (GM fiat). Injuries still apply."
        }
        self.roll_table: Dict = {
            Ability.STR.name: "3d6",
            Ability.CON.name: "3d6",
            Ability.DEX.name: "3d6",
            Ability.INT.name: "3d6",
            Ability.WIS.name: "3d6",
            Ability.CHA.name: "3d6",
        }

    def set_best_ability(self, best_ability: Ability):
        self.roll_table[best_ability] = "4d6h3"
