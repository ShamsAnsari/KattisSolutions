def is_consistant(numbers):
    numbers.sort()
    for i in range(1,len(numbers)):
        try:
            if numbers[i].index(numbers[i-1]) == 0:
                return False
        except ValueError:
            pass
    return True


for t in range(int(input())):
    num_numbers = int(input())
    numbers = []
    for i in range(num_numbers):
        numbers.append(input())

    print("YES" if is_consistant(numbers) else "NO")
