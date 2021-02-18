import math

def sum_divisors(n):
    result = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n // i:
                result += i
            else:
                result += i + n / i
    return result


def get_result(n):
    total = sum_divisors(n)
    if total == n:
        return "perfect"
    if n - 2 <= total <= n + 2:
        return "almost perfect"
    return "not perfect"

try:

    while True:
        line = input()
        if line == "":
            break
        n = int(line)
        print(n, get_result(n))
except EOFError:
    pass
