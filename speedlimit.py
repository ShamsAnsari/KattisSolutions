"""

Difficulty: 1.5
Time: 12 min

Date: 2/14/2021
Author: Shams Ansari
"""

while True:
    n = int(input())
    if n == -1:
        break

    data = []

    for i in range(n):
        distance,  time = map(int, input().split())
        data.append([distance, time])

    total_distance = 0
    prev_time = 0

    for datum in data:
        speed, time = datum
        total_distance += speed * (time - prev_time)
        prev_time = time
    print(str(total_distance) + " miles")
