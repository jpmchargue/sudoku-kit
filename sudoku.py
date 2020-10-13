import math
import sys
import time


def remainingValues(row, col, board):
    options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for r in range(9):
        poi = board[r][col]
        if poi != '.':
            if poi in options:
                options.remove(poi)
    for c in range(9):
        poi = board[row][c]
        if poi != '.':
            if poi in options:
                options.remove(poi)
    box_row = math.floor(row / 3) * 3
    box_col = math.floor(col / 3) * 3
    for i in range(3):
        for j in range(3):
            poi = board[box_row + i][box_col + j]
            if poi != '.':
                if poi in options:
                    options.remove(poi)
    return options


def solveMRV(board):
    minrv = None
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                rv = remainingValues(i, j, board)
                if minrv is None:
                    minrv = ((i, j), rv)
                elif len(rv) < len(minrv[1]):
                    minrv = ((i, j), rv)
    if minrv is None:
        return board
    if len(minrv[1]) <= 0:
        return -1;
    for choice in minrv[1]:
        board_copy = [r[:] for r in board]
        board_copy[minrv[0][0]][minrv[0][1]] = choice
        result = solveMRV(board_copy)
        if result != -1:
            return result
    return -1


start_time = time.time()

with open(sys.argv[1], 'r') as file:
    board = []
    for line in file:
        board.append([c for c in line.split('\n')[0]])

    num_unknowns = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                num_unknowns += 1

    print(f"{81 - num_unknowns} clues, {num_unknowns} unknowns")

    if num_unknowns > 0:
        board = solveMRV(board)

    if board == -1:
        print("This board cannot be solved.")
    else:
        for row in board:
            print(''.join(row))

end_time = time.time()
print(f"Finished in {end_time - start_time} seconds.")
