"""
Tic Tac Toe game

It contains the following functions:
- clear_terminal: clears the terminal
- init_board: initializes the board
- menu: prints the menu and handles the user's choice
- print_board: prints the board
- do_player_turn: handles a player's turn
- is_winner: checks if there is a winner
- is_move_valid: checks if a move is valid
- play: main play loop
- main: main loop
"""

# Importing modules
import os
import sys


def clear_terminal() -> None:
    '''Will clear the terminal'''
    if sys.platform in ('linux', 'darwin'):
        os.system('clear')
    elif sys.platform == 'win32':
        os.system('cls')
    else:
        print("Unsupported OS")


def init_board() -> list:
    '''Returns a 3x3 board with empty spaces'''
    return [[' ' for _ in range(3)] for _ in range(3)]


def menu() -> None:
    '''Prints the menu and handles the user's choice'''
    print("1. Play")
    print("2. Exit")
    choice: int = int(input("Choose an option: "))
    match choice:
        case 1:
            print("Let's play!")
            play()
        case 2:
            print("Bye byee!")
            sys.exit(0)
        case _:
            clear_terminal()
            print("Invalid choice")
            menu()


def print_board(board: list) -> None:
    '''Prints the board'''
    print("--------")
    for row in board:
        print(" |".join(row))
        print("--------")


def do_player_turn(board: list, player_turn: int) -> None:
    '''Handles a player's turn'''
    row_move: int = int(input(f"Player {player_turn}, Enter row: "))
    col_move: int = int(input(f"Player {player_turn}, Enter column: "))
    if is_move_valid(board, row_move, col_move) is False:
        print("Invalid move")
        do_player_turn(board, player_turn)
        player_turn = 2 if player_turn == 1 else 1
    if player_turn == 1:
        board[row_move][col_move] = 'X'
    if player_turn == 2:
        board[row_move][col_move] = 'O'


def is_winner(board: list) -> bool:
    '''Checks if there is a winner'''
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != ' ':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False


def is_move_valid(board: list, row: int, col: int) -> bool:
    '''Checks if a move is valid'''
    return board[row][col] == ' '


def play() -> None:
    '''Main play loop'''
    clear_terminal()
    board: list = init_board()
    print_board(board)
    player_turn: int = 1 # Player 1 starts
    while True:
        do_player_turn(board, player_turn)
        print_board(board)
        if is_winner(board) is True:
            print(f"Player {player_turn} wins!")
            break
        if not any(' ' in row for row in board):
            print("It's a tie!")
            break
        player_turn = 2 if player_turn == 1 else 1


def main() -> None:
    '''Main loop'''
    while True:
        menu()

main()
