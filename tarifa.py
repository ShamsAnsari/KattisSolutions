x = int(input())
n = int(input())
p = [int(input()) for _ in range(n)]
used = sum(p)
total_potential = x * n
print(total_potential - used + x)
