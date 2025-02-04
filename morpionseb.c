#include <stdio.h>
#include <stdlib.h>

void afficher_grille(char grille[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf(" %c ", grille[i][j]);
            if (j < 2) printf("|");
        }
        printf("\n");
        if (i < 2) printf("---|---|---\n");
    }
}

int verifier_victoire(char grille[3][3], char joueur) {
    for (int i = 0; i < 3; i++) {
        if ((grille[i][0] == joueur && grille[i][1] == joueur && grille[i][2] == joueur) ||
            (grille[0][i] == joueur && grille[1][i] == joueur && grille[2][i] == joueur)) {
            return 1;
        }
    }
    if ((grille[0][0] == joueur && grille[1][1] == joueur && grille[2][2] == joueur) ||
        (grille[0][2] == joueur && grille[1][1] == joueur && grille[2][0] == joueur)) {
        return 1;
    }
    return 0;
}

int main() {
    char grille[3][3] = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};
    char joueurs[2] = {'X', 'O'};
    int tour = 0;
    
    while (1) {
        afficher_grille(grille);
        char joueur = joueurs[tour % 2];
        printf("Au tour du joueur %c\n", joueur);
        
        int ligne, colonne;
        while (1) {
            printf("Entrez la ligne et la colonne (0, 1, 2) séparées par un espace : ");
            if (scanf("%d %d", &ligne, &colonne) == 2 && ligne >= 0 && ligne < 3 && colonne >= 0 && colonne < 3 && grille[ligne][colonne] == ' ') {
                grille[ligne][colonne] = joueur;
                break;
            } else {
                printf("Entrée invalide. Réessayez.\n");
                while (getchar() != '\n');
            }
        }
        
        if (verifier_victoire(grille, joueur)) {
            afficher_grille(grille);
            printf("Le joueur %c a gagné !\n", joueur);
            break;
        }
        
        int match_nul = 1;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (grille[i][j] == ' ') {
                    match_nul = 0;
                    break;
                }
            }
        }
        if (match_nul) {
            afficher_grille(grille);
            printf("Match nul !\n");
            break;
        }
        
        tour++;
    }
    return 0;
}
