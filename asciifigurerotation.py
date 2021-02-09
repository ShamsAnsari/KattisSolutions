def print_matrix(matrix):
    for line in matrix:
        for char in line:
            print(char, end="")
        print()


def convert(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == '-':
                matrix[r][c] = '|'
            elif matrix[r][c] == '|':
                matrix[r][c] = '-'


def max_row_length(matrix):
    greatest_row_length = -1
    for r in matrix:
        if greatest_row_length < len(r):
            greatest_row_length = len(r)
    return greatest_row_length


def pad(matrix):
    num_cols_needed = max_row_length(matrix)
    for r in range(len(matrix)):
        if len(matrix[r]) < num_cols_needed:
            difference = num_cols_needed - len(matrix[r])
            for i in range(difference):
                matrix[r].extend(" ")


def matrix_rotated(matrix):
    output = ""
    for c in range(len(matrix[0])):
        for r in range(len(matrix)):
            output += matrix[len(matrix) - r - 1][c]
        output = output.rstrip() + "\n"

    return output


output = ""
while True:
    n = int(input())
    if n == 0:
        break
    matrix = [None] * n
    for i in range(n):
        matrix[i] = list(input())
    pad(matrix)
    convert(matrix)
    output += matrix_rotated(matrix) + "\n"
output = output[:len(output) - 2]
print(output)
