'''This script implements the classic two-player game of "Tic Tac Toe" in the console.
The game provides a clear board layout using the colorama library for enhanced visual distinction.
Players take turns to place their respective markers ('X' or 'O') on the board in an attempt to form a
straight line of three of their markers horizontally, vertically, or diagonally. The game checks for winning
conditions after each move and declares a winner when a player achieves a line of three or when the board is
fully occupied, resulting in a tie. Players are prompted to play again or exit after each game concludes.
'''

from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def display_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print(Fore.YELLOW + '-----------' + Style.RESET_ALL)
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print(Fore.YELLOW + '-----------' + Style.RESET_ALL)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')


def insert_letter(letter, position, board):
    board[position] = letter

def is_space_free(position, board):
    return board[position] == ' '

def is_board_full(board):
    return not any([space == ' ' for space in board[1:]])

def is_winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))

def player_move(board):
    run = True
    while run:
        move = input("Please select a position (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if is_space_free(move, board):
                    run = False
                    insert_letter('X', move, board)
                else:
                    print("Sorry, this space is occupied!")
            else:
                print("Please type a number within the range!")
        except:
            print("Please type a number!")

def computer_move(board):
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board.copy()
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    if 5 in possible_moves:
        move = 5
        return move

    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)
    if corners_open:
        move = select_random(corners_open)
        return move

    if 2 in possible_moves:
        move = 2
        return move
    elif 4 in possible_moves:
        move = 4
        return move
    elif 6 in possible_moves:
        move = 6
        return move
    elif 8 in possible_moves:
        move = 8
        return move

    return move

def select_random(li):
    import random
    ln = len(li)
    return li[random.randrange(0, ln)]

def main():
    print(Fore.CYAN + "Welcome to Tic Tac Toe!" + Style.RESET_ALL)

    # Player choice
    player_letter = input("Do you want to be X or O? ").upper()
    while player_letter not in ['X', 'O']:
        print(Fore.RED + "Invalid choice. Please select either 'X' or 'O'." + Style.RESET_ALL)
        player_letter = input("Do you want to be X or O? ").upper()

    computer_letter = 'O' if player_letter == 'X' else 'X'

    print("Player is", Fore.GREEN + player_letter + Style.RESET_ALL, "and Computer is", Fore.RED + computer_letter + Style.RESET_ALL)

    board = [' ' for x in range(10)]
    while not is_board_full(board):
        if not is_winner(board, computer_letter):
            player_move(board)
            display_board(board)
        else:
            print(Fore.RED + "Computer won this time!" + Style.RESET_ALL)
            return

        if not is_winner(board, player_letter):
            move = computer_move(board)
            if move == 0:
                print(Fore.YELLOW + "Tie Game!" + Style.RESET_ALL)
            else:
                insert_letter(computer_letter, move, board)
                print(f"Computer placed", Fore.RED + computer_letter + Style.RESET_ALL, "in position", move)
                display_board(board)
        else:
            print(Fore.GREEN + "You won this time! Good Job!" + Style.RESET_ALL)
            return

    if is_board_full(board):
        print(Fore.YELLOW + "Tie Game!" + Style.RESET_ALL)

while True:
    main()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
