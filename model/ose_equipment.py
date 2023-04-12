import dice

class_equipment = {
    "Clerc":
        [
            "masse, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, symbole sacré en bois, 1d6 PO",
            "masse, bouclier, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, corde de 15 m, symbole sacré en bois, 1d6 PO",
            "masse, armure de cuir, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, symbole sacré en bois, 5 PO",
            "bâton, armure de cuir, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, 12 pointes de fer, symbole sacré en bois, 3 pieux et maillet, miroir en acier, 2d6 PO",
            "cotte de mailles, marteau de guerre, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 10 pieds, symbole sacré en bois, 2 petits sacs, 2d6 PO",
            "cotte de mailles, bouclier, masse, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, corde de 15 m, symbole sacré en bois, 2 petits sacs, 2d6 PO",
            "cotte de mailles, bouclier, marteau de guerre, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, symbole sacré en bois, 2 petits sacs, 3 pieux et maillet, miroir en acier, 2d6 PO",
            "armure de plaques, bouclier, masse, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, corde de 15 m, symbole sacré en bois, 2d6 PO",
            "armure de plaques, bouclier, marteau de guerre, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, symbole sacré en bois, petit sac, 1d6 PO",
            "armure de plaques, bâton, sac à dos, gourde, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, corde de 15 m, symbole sacré en argent, 1d6 PO",
            "gourdin, 6 torches, sac à dos, outre, 1 semaine de rations de fer, perche de 3m, tue-loup, eau bénite, symbole sacré en bois, parchemin, 2d6 PO",
            "armure de plaques, bouclier, masse, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, corde de 15 m, symbole sacré en argent, 2d6 PO",
            "armure de cuir, masse, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 10 pieds, symbole sacré en bois, parchemin divin aléatoire, 2 flacons d'huile, 1 PO",
            "armure de plaques, bouclier, marteau de guerre, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, corde de 15 m, symbole sacré en argent, 3 pieux et maillet, miroir en acier, 12 PO",
            "cotte de mailles, marteau de guerre, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, symbole sacré en bois, parchemin divin, 10 PO",
            "armure de plaques, bouclier, masse, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, corde de 15 m, symbole sacré en argent, fiole d'eau bénite, 12 pointes de fer, 3 pieux et maillet, petit sac, potion de guérison, 10 PO"]
    ,
    "Nain": []
    ,
    "Voleur": []
    ,
    "Guerrier":
        ["arme d'hast, dague, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, 1d6 PO",
         "gourdin, dague, armure de cuir, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, 1d6 PO",
         "armure de cuir, masse, bouclier, dague, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, 1d6 PO",
         "armure de cuir, hache de combat, hache à main, dague, fronde, pochette avec 20 balles de fronde, 6 torches, sac à dos, outre, 1 semaine de rations de fer, perche de 3m, 2d6 PO",
         "cotte de mailles, lance, bouclier, dague, fronde, pochette avec 20 balles de fronde, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, 3d6 PO",
         "cotte de mailles, bouclier, épée, dague, 6 torches, sac à dos, outre, 1 semaine de rations de fer, perche de 3m, d6 PO",
         "cotte de mailles, épée, arbalète légère, étui avec 30 carreaux, 6 torches, sac à dos, outre, rations de fer pour 1 semaine, corde de 15 m, 3d6 PO",
         "armure de plaques, bouclier, épée, dague, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, d6 PO",
         "armure de plaques, épée à deux mains, 3 dagues, 6 torches, sac à dos, outre, 1 semaine de rations de fer, 15 m de corde, 2 flacons d'huile, 2d6 PO",
         "armure de plaques, bouclier, épée, arbalète, étui avec 30 carreaux, 6 torches, sac à dos, outre, 1 semaine de rations de fer, perche de 3m, d6 PO",
         "armure de plaques, marteau de guerre, dague, arc court, carquois de 20 flèches, 6 torches, sac à dos, outre, rations de fer pour 1 semaine, corde de 15 m, petit sac, 2d6 PO",
         "armure de plaques, bouclier, épée, arbalète, étui avec 30 carreaux, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, d6 PO",
         "armure de plates, arme d'hast, bouclier, épée courte, dague, arbalète légère, étui avec 30 carreaux, 6 torches, sac à dos, outre, rations de fer pour 1 semaine, corde de 15 m, 5 flacons d'huile, 3d6 PO",
         "armure de plaques, épée à deux mains, épée courte, dague, arc long, carquois de 20 flèches, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, 2 petits sacs, 3d6 PO",
         "armure de plaques, arme d'hast, dague, arc long, carquois de 20 flèches, 2 flèches à pointe d'argent, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, corde de 15 m, 3d6 PO",
         "armure de plaques, bouclier, épée, 2 dagues, arbalète légère, étui avec 30 carreaux, 4 carreaux à pointe d'argent, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, 2d6 PO"]
    ,
    "Magicien": []
    ,
    "Hobbit": []
    ,
    "Elfe": []
}


def get_equipment(class_name):
    roll = sum(dice.roll('3d6')) - 3
    eq_list = class_equipment[class_name][roll].split(',')
    has_shield = any('bouclier' in v for v in eq_list)
    armor = next((v for v in eq_list if v in ['armure de plaques', 'cotte de mailles', 'armure de cuir']), '')

    po = 0
    if 'd' in eq_list[-1]:
        to_roll = eq_list[-1].split(' ')[1]
        po = sum(dice.roll(to_roll))
    else:
        po: eq_list[-1].split(' ')[1]
    return eq_list, has_shield, armor, po
