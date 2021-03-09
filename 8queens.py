def print_board():
    for i in range(8):
        print(board[i])

def in_bounds(i,j):
    return 0 <= i < 8 and 0 <= j < 8


def is_valid():
    num_queens = 0
    for row in range(8):
        num_queens_row = sum(board[row])
        if num_queens_row > 1:
            return False
        num_queens += num_queens_row

    if num_queens != 8:
        return False
    for col in range(8):
        sum_col = 0
        for row in range(8):
            sum_col += board[row][col]
        if sum_col > 1:
            return False

    for row in range(8):
        i = row
        j = 0
        sum_diagonal = 0
        while in_bounds(i,j):
            sum_diagonal += board[i][j]
            i -= 1
            j += 1
        if sum_diagonal > 1:
            return False

    for col in range(8):
        i = 7
        j = col
        sum_diagonal = 0
        while in_bounds(i,j):
            sum_diagonal += board[i][j]
            i -= 1
            j += 1
        if sum_diagonal > 1:
            return False


    for row in range(8):
        i = row
        j = 0
        sum_diagonal = 0
        while in_bounds(i,j):
            sum_diagonal += board[i][j]
            i += 1
            j += 1
        if sum_diagonal > 1:
            return False

    for col in range(8):
        i = 0
        j = col
        sum_diagonal = 0
        while in_bounds(i,j):
            sum_diagonal += board[i][j]
            i += 1
            j += 1
        if sum_diagonal > 1:
            return False

    return True



#Init board
board = [None]*8
for i in range(8):
    data = list(input())
    board[i] = [0]*8
    for j in range(8):
        if data[j] == "*":
            board[i][j] = 1



print( "valid" if is_valid() else "invalid")
