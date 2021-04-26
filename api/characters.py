from enum import Enum

from fastapi import APIRouter

from helper import ClassName, Ability
from logic import factory
from logic.character import Character

router = APIRouter()


@router.get("/characters/generate/{a_class}/{name}")
def get_generate(a_class: ClassName, name: str, best_roll_ability: Ability = 'CHA'):

    char_class, race = factory.get_class(a_class)
    c = Character(char_class, race)
    c.ancestry.set_best_ability(best_roll_ability)
    c.generate(name=name)
    return c
