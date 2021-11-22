from heapq import *
num_people, closing_time = map(int, input().split())
line = {}
for i in range(num_people):
    amount, time = map(int, input().split())
    if time in line:
        line[time].append(amount)
    else:
        line[time] = [amount]



time = closing_time
amounts = []
total = 0
while time >= 0 :
    if time in line:
        for amount in line[time]:
            heappush(amounts, -amount)
    time -= 1
    if amounts:
        total += -heappop(amounts)

print(total)

'''
5 4
1 1
1 1
1 1
1 1
10 1000
'''
