# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from char_class import Warrior, DwarfParagon
from character import Character
from ancestry import Elf, Human, Dwarf
from helper import Ability


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   c = Character(Warrior(), Human())
   c.ancestry.set_best_ability(Ability.STR)
   c.generate(name='toto')
   print(c)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
