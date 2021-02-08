columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
rows = [8, 7, 6, 5, 4, 3, 2, 1]


def is_done(board):
    for r in board:
        for c in r:
            if c < 0:
                return False
    return True


def in_bound(r, c):
    return 0 <= r < 8 and 0 <= c < 8


def possible_moves(board, r, c):
    possible = [[r - 2, c - 1], [r - 1, c - 2], [r + 1, c - 2], [r + 2, c - 1], [r + 2, c + 1], [r + 1, c + 2],
                [r - 1, c + 2], [r - 2, c + 1]]
    moves = []
    for possibility in possible:
        if in_bound(*possibility) and board[possibility[0]][possibility[1]] < 0:
            moves.append(possibility)
    return moves


n = int(input())

while n > 0:

    # init board
    board = [None] * 8
    for i in range(8):
        board[i] = [-1] * 8

    # Place Knight
    start_col, start_row = list(input())
    start_row = int(start_row)
    board[rows[start_row - 1] - 1][columns.index(start_col)] = 0

    # Calculate number of steps
    step_num = 1
    r = rows[start_row - 1] - 1
    c = columns.index(start_col)
    moves = possible_moves(board, r, c)
    while not is_done(board):
        # Mark step number
        for i in range(len(moves)):
            r, c = moves[0]
            board[r][c] = step_num
            moves.pop(0)
            moves.extend(possible_moves(board, r, c))
        step_num += 1

    # Find and print Hiding Places
    step_num -= 1
    print(step_num, end=" ")
    for r in range(8):
        for c in range(8):
            if board[r][c] == step_num:
                print(columns[c] + str(rows[r]), end=" ")
    print()

    n -= 1
