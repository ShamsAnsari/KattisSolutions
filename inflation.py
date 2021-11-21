
n = int(input())
canisters = list(map(int, input().split()))

canisters.sort()
least = canisters[-1]/n

for i in range(n):
    ratio = canisters[i] / (i + 1) 
    if ratio > 1:
        print('impossible')
        exit(0)
    if ratio < least:
        least = ratio

print(least)