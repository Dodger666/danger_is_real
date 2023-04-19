from enum import Enum

baseclass = {'pj': '',
     'titre': '',
     'al': '',
     'niv': '',
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
     'for': '',
     'int': '',
     'sag': '',
     'dex': '',
     'con': '',
     'cha': '',
     'forb': '',
     'intb': '',
     'sagb': '',
     'dexb': '',
     'conb': '',
     'chab': '',
     'xp': '0',
     'xpbonus': '',
     'pp': '',
     'po': '',
     'pe': '',
     'pa': '',
     'pc': ''}

cleric = {
     'classe': 'Clerc',
     'prime': 'sag',
     'dv': 'd6',
     'facultes': 'Vade-retro\n1 sort divin de niveau 1 par jour',
     'svmort': '11',
     'savbag': '12',
     'svpara': '14',
     'svsouf': '16',
     'svsort': '15',
     'xpsuiv': '1500',
     'equip1': '',
     'equip2': ''}

dwarf = {
     'classe': 'Nain',
     'prime': 'for',
     'dv': 'd8',
     'facultes': 'Infravision\nDétection des salles piégées 2-6\nDétection architecturale 2-6\nÉcouter aux portes 2-6',
     'svmort': '8',
     'savbag': '9',
     'svpara': '10',
     'svsouf': '13',
     'svsort': '12',
     'xpsuiv': '2200',
     'equip1': '',
     'equip2': ''}

elf = {
     'classe': 'Elfe',
     'prime': '',
     'dv': 'd6',
     'facultes': '1 sort profane de niveau 1 par jour\nInfravision\nDétection des portes secrètes 2-6\nImmunité à la paralysie des goules\nÉcouter aux portes 2-6',
     'svmort': '12',
     'savbag': '13',
     'svpara': '13',
     'svsouf': '15',
     'svsort': '15',
     'xpsuiv': '4000',
     'equip1': '',
     'equip2': ''}

hobbit = {
     'classe': 'Hobbit',
     'prime': '',
     'dv': 'd6',
     'facultes': 'Bonus en +2 CA contre les créatures plus grandes que des humains\nSe cacher: 90% Dans les bois; 2-6 dans les donjons\nÉcouter aux portes 2-6\nBonus +1 aux attaques à distance',
     'svmort': '8',
     'savbag': '9',
     'svpara': '10',
     'svsouf': '13',
     'svsort': '12',
     'xpsuiv': '2000',
     'equip1': '',
     'equip2': ''}

fighter = {
     'classe': 'Guerrier',
     'prime': 'for',
     'dv': 'd8',
     'facultes': '',
     'svmort': '12',
     'savbag': '13',
     'svpara': '14',
     'svsouf': '15',
     'svsort': '16',
     'xpsuiv': '2000',
     'equip1': '',
     'equip2': ''}

magicuser = {
     'classe': 'Magicien',
     'prime': 'int',
     'dv': 'd4',
     'facultes': '1 sort profane de niveau 1 par jour',
     'svmort': '13',
     'savbag': '14',
     'svpara': '13',
     'svsouf': '16',
     'svsort': '15',
     'xpsuiv': '2500',
     'equip1': '',
     'equip2': ''}

thief = {
     'classe': 'Voleur',
     'prime': 'dex',
     'dv': 'd4',
     'facultes': 'Attaque dans le dos (+4/double dégâts)\nCrochetage 15%\nDéplacement silencieux 20%\nDétection ou désamorçage des pièges de trésors 10%\nEscalade de parois à pic 87\nPerception des bruits 2-6\nPickpocket 20%\nSe cacher dans les ombres 10%',
     'svmort': '13',
     'savbag': '14',
     'svpara': '13',
     'svsouf': '16',
     'svsort': '15',
     'xpsuiv': '1200',
     'equip1': '',
     'equip2': ''}

class ose_classes(Enum):
    CLERIC = 'Clerc'
    FIGHTER = 'Guerrier'
    MAGICUSER = 'Magicien'
    THIEF = 'Voleur'
    HOBBIT = 'Hobbit'
    DWARF = 'Nain'
    ELF = 'Elfe'
