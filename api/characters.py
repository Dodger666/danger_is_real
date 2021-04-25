from fastapi import APIRouter
from ancestry import Human
from char_class import Warrior
from character import Character
from helper import Ability

router = APIRouter()


@router.get("/characters/generate/{name}")
def get_generate(name: str):
    c = Character(Warrior(), Human())
    c.ancestry.set_best_ability(Ability.STR.name)
    c.generate(name=name)
    return c
