from math import sqrt


def get_distinct_prime_factors(n):
    factors = set()

    while n % 2 == 0:
        n /= 2
        factors.add(2)

    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            n /= i
            factors.add(i)

    if n > 2:
        factors.add(n)
    return factors


def phi(n):
    factors = get_distinct_prime_factors(n)
    result = n
    for factor in factors:
        result *= (1 - 1 / factor)
    return int(result)


def farey_length(n):
    result = 0
    for i in range(1, n + 1):
        result += phi(i)
    return result + 1


p = int(input())

farey_lengths = [None] * 10001
farey_lengths[1] = 2
for i in range(2, 10001):
    farey_lengths[i] = farey_lengths[i - 1] + phi(i)
while p > 0:
    k, n = [int(data) for data in input().split()]
    print(k, farey_lengths[n])
    p -= 1
