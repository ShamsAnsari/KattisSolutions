def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

def reverse_rows(matrix, num_r):
    for r in range(num_r):
        matrix[r] = matrix[r][::-1]

def reverse_cols(matrix, num_r, num_c):
    for c in range(num_c):
        for r in range(num_r//2):
            matrix[r][c], matrix[num_r - r - 1][c] = matrix[num_r - r - 1][c], matrix[r][c]
    
num_tests = int(input())
x = []
for i in range(num_tests):
    
    num_r, num_c = map(int, input().split())
    matrix = []
    for r in range(num_r):
        matrix.append(list(input()))
    print("Test", i + 1)
    reverse_cols(matrix, num_r, num_c)
    reverse_rows(matrix, num_r)
    print_matrix(matrix)

