"""
Difficulty: 1.5
Time: 15 min
"""

set_num = 1

while True:
    n = int(input())
    if n == 0:
        break
    names = []

    for i in range(n):
        names.append(input())

    print("SET " + str(set_num))

    other_names = []
    i = 0
    while i < n:
        print(names[i])

        if i + 1 < n:
            i += 1
            other_names.append(names[i])
        i += 1

    other_names.reverse()
    for name in other_names:
        print(name)


    set_num += 1

