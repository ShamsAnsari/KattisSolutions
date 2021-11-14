num_tests = int(input())
for _ in range(num_tests):
    n = int(input())
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")
