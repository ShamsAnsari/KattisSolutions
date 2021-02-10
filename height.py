p = int(input())

while p > 0:
    data = [int(data) for data in input().split()]
    k = data.pop(0)
    sorted_data = []

    num_steps = 0
    for student in data:
        i = 0
        while i < len(sorted_data):
            if sorted_data[i] > student:
                break
            i += 1
        num_steps += len(sorted_data) - i
        sorted_data.insert(i, student)
    print(k, num_steps)
    p -= 1
