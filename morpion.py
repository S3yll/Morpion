def check_winner(board):
    # Vérification des lignes et colonnes
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            print(f'GG le joueur: {board[i][0]} a gagné!')
            return False
        if board[0][i] == board[1][i] == board[2][i] != " ":
            print(f'GG le joueur: {board[0][i]} a gagné!')
            return False

    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] != " ":
        print(f'GG le joueur: {board[1][1]} a gagné!')
        return False
    if board[0][2] == board[1][1] == board[2][0] != " ":
        print(f'GG le joueur: {board[1][1]} a gagné!')
        return False

    # Vérification s'il reste des cases vides
    for row in board:
        if " " in row:
            return True
    
    print("Match nul! Aucun gagnant.")
    return False

def draw_board(board):
    print("-------------")
    for row in board:
        print(f'| {row[0]} | {row[1]} | {row[2]} |')
        print("-------------")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    draw_board(board)
    player = 'X'
    
    while True:
        try:
            case = int(input(f"Joueur {player}, entrez un numéro de case (1-9): ")) - 1
            if case not in range(9):
                print("Numéro invalide. Veuillez entrer un nombre entre 1 et 9.")
                continue
            
            x, y = case % 3, case // 3
            if board[y][x] == ' ':
                board[y][x] = player
                draw_board(board)
                if not check_winner(board):
                    break
                player = 'O' if player == 'X' else 'X'
            else:
                print("Case déjà prise! Choisissez une autre case.")
        except ValueError:
            print("Entrée invalide! Veuillez entrer un nombre entre 1 et 9.")

if __name__ == "__main__":
    main()
