
num_elem = int(input())
elems = []
for _ in range(num_elem):
    elems.append(int(input()))

left, right = elems[0] ** 2, sum(elems) - elems[0]
best = left * right
for i in range(1, num_elem):
    left += elems[i] ** 2
    right -= elems[i]

    total = left * right
    best = max(total, best)

print(best)