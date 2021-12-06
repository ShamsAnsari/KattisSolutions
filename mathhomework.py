a, b, c, l = map(int, input().split())

comb = set()
for i in range(l//a + 1):
    for j in range(l//b + 1):
        for k in range(l//c + 1):
            if i*a + j*b+ k*c == l:
                comb.add((i, j, k))

comb = sorted(comb)
for c in comb:
    print(*c)
if len(comb) == 0:
    print('impossible')