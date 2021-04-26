from fastapi import HTTPException
from model.ancestry import Human, Elf, Dwarf, Halfling
from model.char_class import Warrior, Thief, Zealot, Mage, ElfParagon, DwarfParagon, HalflingParagon


def get_class(a_class: str):
    a_class = a_class.lower()

    if a_class == 'warrior':
        return Warrior(), Human()
    if a_class == 'thief':
        return Thief(), Human()
    if a_class == 'zealot':
        return Zealot(), Human()
    if a_class == 'mage':
        return Mage(), Human()
    if a_class == 'elf':
        return ElfParagon(), Elf()
    if a_class == 'dwarf':
        return DwarfParagon(), Dwarf()
    if a_class == 'halfling':
        return HalflingParagon(), Halfling()
    raise HTTPException(status_code=404, detail=f"character class {a_class} not found")