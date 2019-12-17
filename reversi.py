import math
import numpy as np

def check_direction(board, row, column, row_direc, col_direc):
    non_curr = -board[row][column]
    next_row = row + row_direc
    next_column = column + col_direc

    if next_row<0 or next_row>7 or next_column<0 or next_column>7:
        return False
    
    if board[next_row][next_column] != non_curr:
        return False

    while board[next_row][next_column] == non_curr:

        next_row += row_direc
        next_column += col_direc
        if next_row<0 or next_row>7 or next_column<0 or next_column>7:
            return False
          
    if board[next_row][next_column] == board[row][column]:
        return True
    
    return False


def check_position(board, row, column):

    if check_direction(board, row, column, 1, 0):
        return True

    if check_direction(board, row, column, -1, 1):
        return True

    if check_direction(board, row, column, 0, 1):
        return True

    if check_direction(board, row, column, 1, 1):
        return True

    if check_direction(board, row, column, -1, 0):
        return True

    if check_direction(board, row, column, 1, -1):
        return True

    if check_direction(board, row, column, 0, -1):
        return True

    if check_direction(board, row, column, -1, -1):
        return True

    return False


def change_direction(board, row, column, row_direc, col_direc):
    non_curr = -board[row][column]
    next_row = row + row_direc
    next_column = column + col_direc
    count = 0

    if next_row<0 or next_row>7 or next_column<0 or next_column>7:
        return 0
    
    if board[next_row][next_column] != non_curr:
        return 0

    while board[next_row][next_column] == non_curr:
        next_row += row_direc
        next_column += col_direc
        if next_row<0 or next_row>7 or next_column<0 or next_column>7:
            return 0
        
    if board[next_row][next_column] == board[row][column]:
        next_row -= row_direc
        next_column -= col_direc
        while next_row != row or next_column != column:
            board[next_row][next_column] = board[row][column]
            next_row -= row_direc
            next_column -= col_direc
            count += 1
        return count

    return 0

def set_position(board, row, column, mark):
    count = 0
    board[row][column] = mark
    if check_position(board, row, column) == False:
        raise RuntimeError("set_position: not vaild position")
 
    count += change_direction(board, row, column, -1, 0)

    count += change_direction(board, row, column, -1, 1)

    count += change_direction(board, row, column, 0, 1)

    count += change_direction(board, row, column, 1, 1)

    count += change_direction(board, row, column, 1, 0)

    count += change_direction(board, row, column, 1, -1)

    count += change_direction(board, row, column, 0, -1)

    count += change_direction(board, row, column, -1, -1)

    return count


def available_pos(board, current):
    possible_pos = []

    for row in range(8):
        for column in range(8):
            if board[row][column] == 0:
                board[row][column] = current
                if check_position(board, row, column):
                    possible_pos.append((row, column))
                board[row][column] = 0

    return possible_pos

def index_to_char(index):
    if index == -1:
        return 'X'
    elif index == 0:
        return ' '
    elif index == 1:
        return 'O'

def print_board(board):
    char_board = np.vectorize(index_to_char)(board)

    for i in range(8):

        print("     -----------------------------------------------------------------")
        print("     |       |       |       |       |       |       |       |       |")
        
        print("     ", end='')
        for j in range(8):
            print("|   " + char_board[i][j], end='   ')
        
        print('|')
        print("     |       |       |       |       |       |       |       |       |")
    
    print("     -----------------------------------------------------------------\n\n")
