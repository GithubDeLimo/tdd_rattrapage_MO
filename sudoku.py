# Vérifiez si la taille de la grille d'entrée est 9*9
def taille_valide(grille):
    # Si le nombre de lignes est de 9
    if not len(grille) == 9:
        # print("ligne non")
        return False
    else:
        # Le nombre de lignes est de 9, si le nombre de colonnes est de 9
        for i in range(9):
            if not len(grille[i]) == 9:
                # print(i)
                # print(len(grille[i]))
                return False
        return True
