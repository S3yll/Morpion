def afficher_grille(grille):
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 9)

def verifier_victoire(grille):
    # Vérifier les lignes, les colonnes et les diagonales
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != " ":
            return True
        if grille[0][i] == grille[1][i] == grille[2][i] != " ":
            return True
    if grille[0][0] == grille[1][1] == grille[2][2] != " ":
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] != " ":
        return True
    return False

def est_pleine(grille):
    for ligne in grille:
        if " " in ligne:
            return False
    return True

def morpion():
    grille = [[" " for _ in range(3)] for _ in range(3)]
    joueur = "X"

    while True:
        afficher_grille(grille)
        print(f"Joueur {joueur}, entrez votre coup (ligne et colonne) : ")
        
        # Boucle jusqu'à obtenir une entrée valide
        while True:
            try:
                ligne, colonne = map(int, input().split())
                if ligne not in [0, 1, 2] or colonne not in [0, 1, 2]:
                    print("Veuillez entrer des valeurs entre 0 et 2.")
                    continue
                break
            except ValueError:
                print("Entrée invalide. Veuillez entrer deux nombres séparés par un espace.")

        if grille[ligne][colonne] != " ":
            print("Case déjà prise, essayez à nouveau.")
            continue

        grille[ligne][colonne] = joueur

        if verifier_victoire(grille):
            afficher_grille(grille)
            print(f"Joueur {joueur} a gagné !")
            break

        if est_pleine(grille):
            afficher_grille(grille)
            print("Match nul !")
            break

        joueur = "O" if joueur == "X" else "X"

if __name__ == "__main__":
    morpion()