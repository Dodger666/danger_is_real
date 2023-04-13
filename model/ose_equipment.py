import dice

class_equipment = {
    "Clerc":
        [
            " masse, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, symbole sacré en bois, 1d6 PO",
            " masse, bouclier, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, corde de 15 m, symbole sacré en bois, 1d6 PO",
            " masse, armure de cuir, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, symbole sacré en bois, 5 PO",
            " bâton, armure de cuir, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, 12 pointes de fer, symbole sacré en bois, 3 pieux et maillet, miroir en acier, 2d6 PO",
            " cotte de mailles, marteau de guerre, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 10 pieds, symbole sacré en bois, 2 petits sacs, 2d6 PO",
            " cotte de mailles, bouclier, masse, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, corde de 15 m, symbole sacré en bois, 2 petits sacs, 2d6 PO",
            " cotte de mailles, bouclier, marteau de guerre, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, symbole sacré en bois, 2 petits sacs, 3 pieux et maillet, miroir en acier, 2d6 PO",
            " armure de plaques, bouclier, masse, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, corde de 15 m, symbole sacré en bois, 2d6 PO",
            " armure de plaques, bouclier, marteau de guerre, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, symbole sacré en bois, petit sac, 1d6 PO",
            " armure de plaques, bâton, sac à dos, gourde, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, corde de 15 m, symbole sacré en argent, 1d6 PO",
            " gourdin, 6 torches, sac à dos, outre, 1 semaine de rations de fer, perche de 3m, tue-loup, eau bénite, symbole sacré en bois, parchemin, 2d6 PO",
            " armure de plaques, bouclier, masse, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, corde de 15 m, symbole sacré en argent, 2d6 PO",
            " armure de cuir, masse, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 10 pieds, symbole sacré en bois, parchemin divin aléatoire, 2 flacons d'huile, 1 PO",
            " armure de plaques, bouclier, marteau de guerre, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, corde de 15 m, symbole sacré en argent, 3 pieux et maillet, miroir en acier, 12 PO",
            " cotte de mailles, marteau de guerre, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, symbole sacré en bois, parchemin divin, 10 PO",
            " armure de plaques, bouclier, masse, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, corde de 15 m, symbole sacré en argent, fiole d'eau bénite, 12 pointes de fer, 3 pieux et maillet, petit sac, potion de guérison, 10 PO"]
    ,
    "Nain": [
        " armure de cuir, hache de guerre, dague, 6 torches, sac à dos, outre, 1 semaine de rations de fer, corde de 15 m, d6 PO",
        " armure de cuir, hache, bouclier, 6 torches, sac à dos, outre, 1 semaine de rations de fer, perche de 3m, d6 PO",
        " cotte de mailles, marteau de guerre, bouclier, dague, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, d6 PO",
        " cotte de mailles, hache de combat, hache à main, dague, fronde, pochette avec 20 balles de fronde, 6 torches, sac à dos, outre, 1 semaine de rations de fer, perche de 3m, 2d6 PO",
        " cotte de mailles, hache, bouclier, dague, fronde, pochette avec 20 balles de fronde, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, 3d6 PO",
        " cotte de mailles, hache de combat, bouclier, hache, dague, 6 torches, sac à dos, outre, 1 semaine de rations de fer, perche de 10 pieds, d6 PO",
        " armure de plaques, arme d'hast, hache, arbalète, étui avec 30 carreaux, 6 torches, sac à dos, outre, rations de fer pour 1 semaine, corde de 15 m, 3d6 PO",
        " armure de plaques, bouclier, hache, dague, 6 torches, sac à dos, outre, 1 semaine de rations de fer, perche de 3m, d6 PO",
        " armure de plaques, hache de guerre, marteau de guerre, bouclier, 3 dagues, 6 torches, sac à dos, outre, 1 semaine de rations de fer, 15 m de corde, 2 flacons d'huile, 2d6 PO",
        " armure de plaques, bouclier, hache, arbalète, étui avec 30 carreaux, 6 torches, sac à dos, outre, 1 semaine de rations de fer, perche de 3m, d6 PO",
        " armure de plaques, hache de combat, dague, arbalète 35, étui avec 30 carreaux, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, petit sac, 2d6 PO",
        " armure de plaques, bouclier, marteau de guerre, arbalète, étui avec 30 carreaux, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, d6 PO",
        " armure de plaques, casque, 2 haches de combat, dague, arbalète, mallette de 30 carreaux, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, 15 m de corde, 5 flacons d'huile, 3d6 PO",
        " armure de plaques, épée à deux mains, dague, arbalète, étui de 30 carreaux, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, 2 petits sacs, 3d6 PO",
        " armure de plaques, arme d'hast, hache, dague, arbalète, étui avec 30 carreaux, 2 carreaux à pointe d'argent, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, 15 m de corde, 3d6 PO",
        " armure de plaques, bouclier, marteau de guerre, 2 dagues, arbalète, étui avec 30 carreaux, 4 carreaux à pointe d'argent, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, 2d6 PO"
    ]
    ,
    "Voleur": [
        " club, fronde, pochette avec 20 balles de fronde, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, d6 PO",
        " masse, armure de cuir, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, 2 petits sacs, d6 PO",
        " masse, dague, fronde, pochette avec 20 balles de fronde, armure en cuir, 6 torches, sac à dos, outre, rations de fer pour 1 semaine, corde de 15 m, 2d6 PO",
        " épée, dague, armure de cuir, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, 2d6 PO",
        " gourdin, arbalète légère, étui avec 30 carreaux, armure de cuir, 6 torches, sac à dos, outre, 1 semaine de rations de fer, corde de 15 m, 2 petits sacs, 2d6 PO",
        " épée, arbalète légère, étui de 30 carreaux, armure de cuir, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, 1 sac de caltrops, perche de 3m, 2d6 PO",
        " épée, 2 dagues, arc court 35, carquois de 20 flèches, armure de cuir, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, d6 PO",
        " épée, dague, armure de cuir, sac à dos, gourde, lanterne, 4 flacons d'huile, 1 sac caltrops, 1 semaine de rations de fer, 3m perche, 2 petits sacs, 10d6 PO",
        " épée, arbalète, étui de 30 carreaux, 2 carreaux à pointe d'argent, armure de cuir, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, 15 m de corde, 2d6 PO",
        " épée, dague, arc court, carquois de 20 flèches, armure de cuir, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, 6d6 PO",
        " épée, armure de cuir, sac à dos, gourde, lanterne, 4 flacons d'huile, 1 sac caltrops, 1 semaine de rations de fer, 15 m de corde, 20d6 PO",
        " épée, dague, arbalète, étui de 30 carreaux, 6 carreaux à pointe d'argent, armure de cuir, sac à dos, gourde, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, 4d6 PO",
        " épée, dague, arc court, carquois de 20 flèches, 6 flèches à pointe d'argent, armure de cuir, sac à dos, gourde, lanterne, 1 sac caltrops, 4 flacons d'huile, 1 semaine de rations de fer, 15 m de corde, 6d6 PO",
        " épée, 4 dagues, armure de cuir, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, 2 petits sacs, 20d6 PO",
        " épée, 3 dagues, arbalète, étui de 30 carreaux, armure de cuir, sac à dos, gourde, lanterne, 1 sac caltrops, 4 flacons d'huile, rations de fer pour 1 semaine, corde de 15 m, petit sac, 20d6 PO",
        " épée, 1 dague d'argent, arc court, carquois de 20 flèches, 8 flèches à pointe d'argent, armure de cuir, sac à dos, gourde, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, 2 petits sacs, perche de 3m, 6d6 PO"]
    ,
    "Guerrier":
        [" arme d'hast, dague, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, 1d6 PO",
         " gourdin, dague, armure de cuir, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, 1d6 PO",
         " armure de cuir, masse, bouclier, dague, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, 1d6 PO",
         " armure de cuir, hache de combat, hache à main, dague, fronde, pochette avec 20 balles de fronde, 6 torches, sac à dos, outre, 1 semaine de rations de fer, perche de 3m, 2d6 PO",
         " cotte de mailles, lance, bouclier, dague, fronde, pochette avec 20 balles de fronde, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, 3d6 PO",
         " cotte de mailles, bouclier, épée, dague, 6 torches, sac à dos, outre, 1 semaine de rations de fer, perche de 3m, d6 PO",
         " cotte de mailles, épée, arbalète légère, étui avec 30 carreaux, 6 torches, sac à dos, outre, rations de fer pour 1 semaine, corde de 15 m, 3d6 PO",
         " armure de plaques, bouclier, épée, dague, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, d6 PO",
         " armure de plaques, épée à deux mains, 3 dagues, 6 torches, sac à dos, outre, 1 semaine de rations de fer, 15 m de corde, 2 flacons d'huile, 2d6 PO",
         " armure de plaques, bouclier, épée, arbalète, étui avec 30 carreaux, 6 torches, sac à dos, outre, 1 semaine de rations de fer, perche de 3m, d6 PO",
         " armure de plaques, marteau de guerre, dague, arc court, carquois de 20 flèches, 6 torches, sac à dos, outre, rations de fer pour 1 semaine, corde de 15 m, petit sac, 2d6 PO",
         " armure de plaques, bouclier, épée, arbalète, étui avec 30 carreaux, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, d6 PO",
         " armure de plaques, arme d'hast, bouclier, épée courte, dague, arbalète légère, étui avec 30 carreaux, 6 torches, sac à dos, outre, rations de fer pour 1 semaine, corde de 15 m, 5 flacons d'huile, 3d6 PO",
         " armure de plaques, épée à deux mains, épée courte, dague, arc long, carquois de 20 flèches, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, 2 petits sacs, 3d6 PO",
         " armure de plaques, arme d'hast, dague, arc long, carquois de 20 flèches, 2 flèches à pointe d'argent, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, corde de 15 m, 3d6 PO",
         " armure de plaques, bouclier, épée, 2 dagues, arbalète légère, étui avec 30 carreaux, 4 carreaux à pointe d'argent, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, 2d6 PO"]
    ,
    "Magicien":
        [" dague, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, d6 PO",
         " bâton, 2 dagues, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, 2 flacons d'huile, 15 m de corde, 2d6 PO",
         " dague, sac à dos, gourde, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, 2d6 PO",
         " bâton, dague, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, corde de 15 m, fiole d'eau bénite, 2d6 PO",
         " 2 dagues, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3 m, 5 flacons d'huile, miroir d'argent, belladona, 2d6 PO",
         " bâton, dague, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, 15 m de corde, 2 fioles d'eau bénite, d6 PO",
         " 3 dagues, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, fiole d'eau bénite, 5d6 PO",
         " dague, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, 15 m de corde, 2 fioles d'eau bénite, 6d6 PO",
         " dague, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, 20d6 PO",
         " bâton, dague, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, corde de 15 m, 20d6 PO",
         " dague, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, parchemin arcanique, perche de 3m, 4 PO",
         " 2 dagues, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, parchemin arcanique, corde de 15 m, 2d6 PO",
         " dague, sac à dos, gourde, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, parchemin arcanique, perche de 3m, d6 PO",
         " bâton, dague, sac à dos, gourde, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, parchemin arcanique, corde de 15 m, 4d6 PO",
         " dague en argent, sac à dos, gourde, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, parchemin arcanique, perche de 3m, 5d6 PO",
         " bâton, dague en argent, sac à dos, gourde, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, parchemin arcanique, corde de 15 m, 20d6 PO"]
    ,
    "Hobbit": [" masse, dague, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, d6 PO",
               " masse, armure de cuir, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, d6 PO",
               " armure de cuir, masse, bouclier, dague, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, d6 PO",
               " armure de cuir, hache, dague, fronde, pochette avec 20 balles de fronde, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, perche de 3m, 2d6 PO",
               " cotte de mailles, épée courte, bouclier, dague, fronde, pochette avec 20 balles de fronde, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, 3d6 PO",
               " cotte de mailles, bouclier, épée courte, dague, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, perche de 3m, d6 PO",
               " cotte de mailles, épée courte, arc court, carquois de 20 flèches, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, 3d6 PO",
               " cotte de mailles, bouclier, épée courte, dague, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, perche de 3m, d6 PO",
               " cotte de mailles, épée courte, 3 dagues, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, 15 m de corde, 2 flacons d'huile, 2d6 PO",
               " armure de plaques, bouclier, épée courte, arbalète, étui avec 30 carreaux, 6 torches, sac à dos, outre, 1 semaine de rations de fer, perche de 3m, d6 PO",
               " armure de plaques, épée courte, dague, arc court, carquois de 20 flèches, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, petit sac, 2d6 PO",
               " armure de plaques, bouclier, épée courte, arbalète, étui avec 30 carreaux, sac à dos, outre, lanterne, 4 flacons d'huile, 1 sac caltrops, 1 semaine de rations de fer, perche de 3m, d6 PO",
               " armure de plaques, bouclier, épée courte, dague, arc court, carquois de 20 flèches, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, 15 m de corde, 5 flacons d'huile, 3d6 PO",
               " armure de plaques, épée courte, dague, arc court, carquois de 20 flèches, sac à dos, outre, lanterne, 4 flacons d'huile, 1 sac caltrops, 1 semaine de rations de fer, perche de 3m, 2 petits sacs, 3d6 PO",
               " armure de plaques, bouclier, épée courte, dague d'argent, arc court, carquois de 20 flèches, 2 flèches à pointe d'argent, sac à dos, gourde, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, corde de 15 m, 3d6 PO",
               " armure de plaques, bouclier, épée courte, 2 dagues, arbalète, étui avec 30 carreaux, 4 carreaux à pointe d'argent, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, 2d6 PO"]
    ,
    "Elfe": [
        " armure de cuir, épée, dague, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, corde de 15 m, d6 PO",
        " armure de cuir, lance, dague, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, d6 PO",
        " armure de cuir, lance, bouclier, dague, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, corde de 15 m, d6 PO",
        " armure de cuir, bouclier, épée courte, dague, arc court, carquois de 20 flèches, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, perche de 3m, 2d6 PO",
        " cotte de mailles, lance, bouclier, dague, arc court, carquois de 20 flèches, 6 torches, sac à dos, outre, rations de fer pour 1 semaine, corde de 15 m, 3d6 PO",
        " cotte de mailles, bouclier, épée, dague, 6 torches, sac à dos, outre, 1 semaine de rations de fer, perche de 3m, d6 PO",
        " cotte de mailles, lance, arc long, carquois de 20 flèches, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, corde de 15 m, 3d6 PO",
        " armure de plaques, bouclier, épée, dague, 6 torches, sac à dos, gourde, 1 semaine de rations de fer, perche de 3m, d6 PO",
        " armure de plaques, épée à deux mains, épée courte, 3 dagues, 6 torches, sac à dos, outre, rations de fer pour 1 semaine, corde de 15 m, 2 flacons d'huile, 2d6 PO",
        " armure de plaques, bouclier, épée, arc long, carquois de 20 flèches, 6 torches, sac à dos, gourde, rations de fer pour 1 semaine, perche de 3m, d6 PO",
        " armure de plaques, épée, dague, arc court 35, carquois de 20 flèches, 6 torches, sac à dos, outre, rations de fer pour 1 semaine, corde de 15 m, petit sac, 2d6 PO",
        " armure de plaques, bouclier, épée, arc long, carquois de 20 flèches, dague, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3m, d6 PO",
        " armure de plaques, bouclier, épée, dague, arc long, carquois de 20 flèches, 6 torches, sac à dos, outre, 1 semaine de rations de fer, 15 m de corde, 5 flacons d'huile, 3d6 PO",
        " armure de plaques, épée à deux mains, dague, arc court, carquois de 20 flèches, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3 mètres, 2 petits sacs, parchemin arcanique, 3d6 PO",
        " armure de plaques, lance, dague, arc long, carquois de 20 flèches, 2 flèches à pointe d'argent, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, corde de 15 m, 3d6 PO",
        " armure de plaques, bouclier, épée, 2 dagues, arc long, carquois de 20 flèches, 4 carreaux à pointe d'argent, sac à dos, outre, lanterne, 4 flacons d'huile, 1 semaine de rations de fer, perche de 3 mètres, parchemin arcanique, 2d6 PO"]
}


def get_equipment(class_name):
    roll = sum(dice.roll('3d6')) - 3
    eq_list = class_equipment[class_name][roll].split(',')
    has_shield = any('bouclier' in v for v in eq_list)
    armor = next((v.strip() for v in eq_list if v.strip() in ['armure de plaques', 'cotte de mailles', 'armure de cuir']), '')

    po = 0
    if 'd' in eq_list[-1]:
        to_roll = eq_list[-1].split(' ')[1]
        po = sum(dice.roll(to_roll))
    else:
        po: eq_list[-1].split(' ')[1]
    return eq_list, has_shield, armor, po
