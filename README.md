# Game-Project

main.py:

Ce fichier contient le programme principal pour jouer à un jeu de combat. Il utilise des fonctions importées à partir d'un fichier appelé "utils.py" pour jouer le jeu, gérer les scores et stocker les scores dans un fichier.
Il y a deux types de choix pour le joueur : attaquer ou boire une potion. Puis c'est au tour de l'ennemi d'infliger les dégats.
Il y a aussi un menu principal pour jouer un nouveau jeu ou quitter le jeu.

Il est important de noter que le fichier "utils.py" doit être présent dans le même répertoire que ce fichier pour que le programme fonctionne correctement.

utils.py:

Ce fichier contient des fonctions pour jouer le jeu et gérer les scores d'un jeu de combat.

Les fonctions incluent :
    no_one_is_dead: vérifie si un joueur ou l'ennemi est mort
    attack: gère les attaques des joueurs et de l'ennemi et met à jour les scores en conséquence
    drink_potion: gère la consommation des potions par le joueur et met à jour les scores en conséquence
    display_scores: affiche les scores actuels des joueurs et de l'ennemi
    who_won: détermine qui a gagné la partie et met à jour les scores de victoires
    create_file: crée un fichier pour stocker les scores si il n'existe pas
    store_scores: stocke les scores de la partie dans un fichier.
    total_score: stocke le nombre total de victoires de chaque joueurs dans le fichier à la fin du jeu.
    menu: propose au joueur d'attaquer ou de boire une potion
    principal_menu: proposer au joueur de jouer une autre manche ou de quitter le jeu.