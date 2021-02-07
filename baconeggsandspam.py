while True:
    n = int(input())
    if n == 0:
        break
    data = {}
    while n > 0:
        line = input().split(" ")
        name = line.pop(0)
        for dish in line:
            if dish in data:
                data[dish].append(name)
            else:
                data[dish] = [name]
        n -= 1
    for food in sorted(data):
        print(food, end=" ")
        for name in sorted(data[food]):
            print(name, end=" ")
        print()
    print()
