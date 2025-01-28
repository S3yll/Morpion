#include <stdio.h>

#define SIZE 3

void afficherGrille(char grille[SIZE][SIZE]) {
    printf("\n");
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            printf(" %c ", grille[i][j]);
            if (j < SIZE - 1) printf("|");
        }
        printf("\n");
        if (i < SIZE - 1) printf("---+---+---\n");
    }
    printf("\n");
}

int verifierGagnant(char grille[SIZE][SIZE], char joueur) {
    for (int i = 0; i < SIZE; i++) {
        // Vérifie les lignes et les colonnes
        if ((grille[i][0] == joueur && grille[i][1] == joueur && grille[i][2] == joueur) ||
            (grille[0][i] == joueur && grille[1][i] == joueur && grille[2][i] == joueur)) {
            return 1;
        }
    }
    // Vérifie les diagonales
    if ((grille[0][0] == joueur && grille[1][1] == joueur && grille[2][2] == joueur) ||
        (grille[0][2] == joueur && grille[1][1] == joueur && grille[2][0] == joueur)) {
        return 1;
    }
    return 0;
}

int grillePleine(char grille[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (grille[i][j] == ' ') return 0;
        }
    }
    return 1;
}

void jouerTour(char grille[SIZE][SIZE], char joueur) {
    int ligne, colonne;
    while (1) {
        printf("Joueur %c, entrez votre ligne 1 a 3 : ",joueur);
        scanf("%d", &ligne);
        printf("entrer votre colonne 1 a 3 : ");
        scanf("%d", &colonne);
        ligne--; // Ajuste pour indexation de 0
        colonne--;
        if (ligne >= 0 && ligne < SIZE && colonne >= 0 && colonne < SIZE && grille[ligne][colonne] == ' ') {
            grille[ligne][colonne] = joueur;
            break;
        } else {
            printf("Coup invalide, réessayez.\n");
        }
    }
}

int main() {
    char grille[SIZE][SIZE] = {
        {' ', ' ', ' '},
        {' ', ' ', ' '},
        {' ', ' ', ' '}
    };

    char joueurActuel = 'X';
    printf("Bienvenue dans le jeu de Morpion !\n");

    while (1) {
        afficherGrille(grille);
        jouerTour(grille, joueurActuel);

        if (verifierGagnant(grille, joueurActuel)) {
            afficherGrille(grille);
            printf("Félicitations ! Le joueur %c a gagné !\n", joueurActuel);
            break;
        }

        if (grillePleine(grille)) {
            afficherGrille(grille);
            printf("Match nul !\n");
            break;
        }

        joueurActuel = (joueurActuel == 'X') ? 'O' : 'X';
    }

    return 0;
}