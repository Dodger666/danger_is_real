import random
import dice
import math


GEMS_JEWELRY = []
MINOR_MAGIC_ITEMS = []
MEDIUM_MAGIC_ITEMS = []
MAJOR_MAGIC_ITEMS = []


def get_cursed_scroll():
    return 'cursed scroll'

def get_protection_scroll():
    return 'protection scroll'
def get_magic_user_spell(level: int):

    spell_list = {
    1: [
    'Charm Person	',
    'Detect Magic	',
    'Hold Portal	',
    'Light	',
    'Magic Missile	',
    'Protection from Evil	',
    'Read Languages	',
    'Read Magic	',
    'Shield	',
    'Sleep	'],
    2:[
    'Continual Light	',
    'Darkness, 15-foot Radius	',
    'Detect Evil	',
    'Detect Invisibility	',
    'ESP	',
    'Invisibility	',
    'Knock	',
    'Levitate	',
    'Locate Object	',
    'Magic Mouth	',
    'Mirror Image	',
    'Phantasmal Force	',
    'Pyrotechnics	',
    'Strength	',
    'Web	',
    'Wizard Lock	'],
    3:[
    'Clairaudience	',
    'Clairvoyance	',
    'Darkvision	',
    'Dispel Magic	',
    'Explosive Runes	',
    'Fireball	',
    'Fly	',
    'Haste	',
    'Hold Person	',
    'Invisibility, 10-foot Radius	',
    'Lightning Bolt	',
    'Monster Summoning I	',
    'Protection from Evil, 10-foot	',
    'Radius	',
    'Protection from Normal Missiles	',
    'Rope Trick	',
    'Slow	',
    'Suggestion	',
    'Water Breathing	'],
    4:[
    'Charm Monster	',
    'Confusion	',
    'Dimension Door	',
    'Extension I	',
    'Fear	',
    'Hallucinatory Terrain	',
    'Ice Storm	',
    'Massmorph	',
    'Monster Summoning II	',
    'Plant Growth	',
    'Polymorph Other	',
    'Polymorph Self	',
    'Remove Curse	',
    'Wall of Fire	',
    'Wall of Ice	',
    'Wizard Eye	'],
    5:[
    'Animal Growth	',
    'Animate Dead	',
    'Cloudkill	',
    'Conjuration of Elementals	',
    'Contact Other Plane	',
    'Extension II	',
    'Feeblemind	',
    'Hold Monster	',
    'Magic Jar	',
    'Monster Summoning III	',
    'Passwall	',
    'Telekinesis	',
    'Teleport	',
    'Transmute Rock to Mud	',
    'Wall of Iron	',
    'Wall of Stone	'],
    6:[
    'Anti-Magic Shell	',
    'Control Weather	',
    'Death Spell	',
    'Disintegrate	',
    'Enchant Item	',
    'Extension III	',
    'Geas	',
    'Invisible Stalker	',
    'Legend Lore	',
    'Lower Water	',
    'Monster Summoning IV	',
    'Move Earth	',
    'Part Water	',
    'Project Image	',
    'Reincarnation	',
    'Repulsion	',
    'Stone to Flesh	'],
    7:[
    'Charm Plants	',
    'Conjuration of Demons	',
    'Delayed Blast Fireball	',
    'Limited Wish	',
    'Mass Invisibility	',
    'Monster Summoning V	',
    'Phase Door	',
    'Power Word, Stun	',
    'Reverse Gravity	',
    'Simulacrum	'],
    8:[
    'Clone	',
    'Mass Charm	',
    'Mind Blank	',
    'Monster Summoning VI	',
    'Permanency	',
    'Polymorph Object	',
    'Power Word, Blind	',
    'Symbol	'],
    9:[
    'Astral Spell	',
    'Maze	',
    'Gate	',
    'Meteor Swarm	',
    'Monster Summoning VII	',
    'Power Word, Kill	',
    'Prismatic Sphere	',
    'Shape Change	',
    'Time Stop	',
    'Wish	']
    }
    return random.choice(spell_list[level])



def table_79_minor_gems_and_jewelry():
    dice_result = int(dice.roll('1d4'))
    if dice_result == 1:
        return [f'Gem or jewelry worth {int(dice.roll("1d6"))} gp']
    if dice_result == 2:
        return [f'Gem or jewelry worth {int(dice.roll("1d100+25"))} gp']
    if dice_result == 3:
        return [f'Gem or jewelry worth {int(dice.roll("1d100+75"))} gp']
    if dice_result == 4:
        return [f'Gem or jewelry worth {int(dice.roll("1d100*10"))} gp']


def table_80_medium_gems_and_jewelry():
    dice_result = int(dice.roll('1d4'))
    if dice_result == 1:
        return [f'Gem or jewelry worth {int(dice.roll("1d100"))} gp']
    if dice_result == 2:
        return [f'Gem or jewelry worth {int(dice.roll("1d6*200"))} gp']
    if dice_result == 3:
        return [f'Gem or jewelry worth {int(dice.roll("1d6*300"))} gp']
    if dice_result == 4:
        return [f'Gem or jewelry worth {int(dice.roll("1d100*100"))} gp']


def table_81_major_gems_and_jewelry():
    dice_result = int(dice.roll('1d4'))
    if dice_result == 1:
        return [f'Gem or jewelry worth {int(dice.roll("1d100*10"))} gp']
    if dice_result == 2:
        return [f'Gem or jewelry worth {int(dice.roll("1d100*80"))} gp']
    if dice_result == 3:
        return [f'Gem or jewelry worth {int(dice.roll("1d100*120"))} gp']
    if dice_result == 4:
        return [f'Gem or jewelry worth {int(dice.roll("1d100*200"))} gp']


def table_82_minor_magic_items():
    dice_result = int(dice.roll('1d4'))
    if dice_result == 1:
        return table_85_potions()
    if dice_result == 2:
        return table_86_scrolls()
    if dice_result == 3:
        return []
    if dice_result == 4:
        return []


def table_85_potions():
    table_potions = {
        '3':
            'Animal Control',
        '6':
            'Clairaudience',
        '9':
            'Clairvoyance',
        '12':
            'Diminution',
        '15':
            'Dragon Control',
        '18':
            'Ethereality',
        '21':
            'Fire Resistance',
        '24':
            'Flying',
        '25':
            'Frozen Concoction',
        '27':
            'Gaseous Form',
        '30':
            'Giant Strength',
        '33':
            'Growth',
        '36':
            'Heroism',
        '39':
            'Invisibility',
        '42':
            'Invulnerability',
        '45':
            'Levitation',
        '48':
            'Plant Control',
        '55':
            'Poison',
        '58':
            'Slipperiness',
        '61':
            'Treasure Finding',
        '64':
            'Undead Control',
        '75':
            'Extra Healing',
        '100':
            'Healing'}
    dice_result = int(dice.roll('1d100'))
    return [next((pv for pk, pv in table_potions.items() if dice_result <= int(pk)))]


def table_86_scrolls(dice_type: str):
    dice_result = int(dice.roll(dice_type))
    # tuple (nb of spell, level each)
    if dice_result == 1:
        return [get_magic_user_spell(1)]
    if dice_result == 2:
        return [get_magic_user_spell(int(dice.roll('1d3')))]
    if dice_result == 3:
        return [get_magic_user_spell(int(dice.roll('1d2'))), get_magic_user_spell(int(dice.roll('1d2')))]
    if dice_result == 4:
        return [get_magic_user_spell(1), get_magic_user_spell(1), get_magic_user_spell(1)]
    if dice_result == 5:
        return [get_cursed_scroll()]
    if dice_result == 6:
        return [get_protection_scroll()]

def generate_treasure_hoard(total_xp: int):
    total_gold = int(dice.roll('1d3+1')) * total_xp
    split_trade_out(total_gold)


def split_trade_out(total_gold: int):
    nb_possible_100_tradeout = math.floor(total_gold / 100)
    nb_possible_1000_tradeout = math.floor(total_gold / 1000)
    nb_possible_5000_tradeout = math.floor(total_gold / 5000)
    print('posible tradeout', nb_possible_100_tradeout, nb_possible_1000_tradeout, nb_possible_5000_tradeout)

    nb_100_tradeout = actual_tradeout(nb_possible_100_tradeout)
    nb_1000_tradeout = actual_tradeout(nb_possible_1000_tradeout)
    nb_5000_tradeout = actual_tradeout(nb_possible_5000_tradeout)
    print('actual tradeout', nb_100_tradeout, nb_1000_tradeout, nb_5000_tradeout)

    total_tradeout = (nb_100_tradeout * 100) + (nb_1000_tradeout * 1000) + (nb_5000_tradeout * 5000)
    final_gold = total_gold - total_tradeout
    if total_tradeout > total_gold:
        # major treasure
        final_gold = total_gold
    print('final gold', final_gold)

    get_100_tradeout(nb_100_tradeout)

    print('GEMS_JEWELRY', GEMS_JEWELRY)
    print('MINOR_MAGIC_ITEMS', MINOR_MAGIC_ITEMS)


def get_100_tradeout(nb_100_tradeout):

    for t in range(0, nb_100_tradeout):
        if int(dice.roll('1d20')) == 20:
            MINOR_MAGIC_ITEMS.extend(table_82_minor_magic_items())
        GEMS_JEWELRY.extend(table_79_minor_gems_and_jewelry())


def actual_tradeout(nb_possible):
    tot_tradeout = 0
    for t in range(0, nb_possible):
        if int(dice.roll('1d10')) == 1:
            tot_tradeout += 1
    return tot_tradeout


if __name__ == '__main__':
    #generate_treasure_hoard(3500)
    print(table_86_scrolls('1d6'))
