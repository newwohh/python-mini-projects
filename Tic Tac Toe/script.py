import random

test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


def display_board(board):
    print('\n'*100)
    # print(board[7] + "|" + board[8] + "|" + board[9])
    # print(board[4] + "|" + board[5] + "|" + board[6])
    # print(board[1] + "|" + board[2] + "|" + board[3])
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    marker = ''

    while not (marker == "X" or marker == "O"):
        marker = input("Player 1: Choose X or O: ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def choose_first():

    if random.randint(0, 1) == 0:
        return "Player 2"
    else:
        return "Player 1"


def space_check(board, position):
    return board[position] == ''


def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


def player_choice():
    position = 0
    position = int(input('Choose position: (1-9)'))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print("Welcome to My Tic Tac Toe")


while True:
    position = 0
    board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play! y or n ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            while turn == 'Player 1':
                display_board(board)
                position = int(input('Choose position: (1-9)'))
                place_marker(board, player1_marker, position)
                turn = "Player 2"

                if win_check(board, player1_marker):
                    display_board(board)
                    print('Player 1 won!')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print("Tie")
                        break
                    else:
                        turn = "Player 2"

        else:
            while turn == 'Player 2':
                display_board(board)
                position = int(input('Choose position: (1-9)'))
                place_marker(board, player2_marker, position)
                turn = "Player 2"

                if win_check(board, player2_marker):
                    display_board(board)
                    print('Player 2 won!')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print("Tie")
                        break
                    else:
                        turn = "Player 1"

    if not replay():
        break
