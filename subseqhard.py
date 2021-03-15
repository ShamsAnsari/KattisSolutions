
for i in range(int(input())):
    input()
    n = int(input())
    arr = list(map(int, input().split()))


    count = 0
    sums = {}
    total = 0
    sums[0] = 1
    for i in range(n):
        total += arr[i]
        sums[total] = sums.get(total, 0) + 1
        if total - 47 in sums:
            count += sums[total - 47]
    print(count)
