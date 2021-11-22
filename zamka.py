def sum_digits(num):
    return sum(list(map(int, list(str(num)))))

lower_bound = int(input())
upper_bound = int(input())
X = int(input())


N = 0
for i in range(lower_bound, upper_bound + 1):
    if sum_digits(N) == X:
        break
    N = i

M = 0
for i in range(lower_bound, upper_bound + 1)[::-1]:
    if sum_digits(i) == X:
        M = i
        break


print(N)
print(M)