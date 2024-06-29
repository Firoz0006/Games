import numpy as np

# Initial board setup
board = np.array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
p1s = 'X'
p2s = 'O'

def place(symbol):
    print(np.matrix(board))
    while True:
        try:
            row = int(input("Enter row (1, 2, 3): ")) - 1
            col = int(input("Enter column (1, 2, 3): ")) - 1
            if row in range(3) and col in range(3) and board[row][col] == '-':
                break
            else:
                print('Invalid input. Please enter again.')
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 3.')
    board[row][col] = symbol

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)

def check_rows(symbol):
    for r in range(3):
        if all([board[r][c] == symbol for c in range(3)]):
            print(symbol, 'Won the game')
            return True
    return False

def check_cols(symbol):
    for c in range(3):
        if all([board[r][c] == symbol for r in range(3)]):
            print(symbol, 'Won the game')
            return True
    return False

def check_diagonals(symbol):
    if all([board[i][i] == symbol for i in range(3)]) or all([board[i][2-i] == symbol for i in range(3)]):
        print(symbol, 'Won')
        return True
    return False

def play():
    for turn in range(9):
        if turn % 2 == 0:
            print('X turn')
            place(p1s)
            if won(p1s):
                break
        else:
            print('O turn')
            place(p2s)
            if won(p2s):
                break
    else:
        print('DRAW')

play()
