x, y, n = list(map(int, input().split()))

for i in range(1, n + 1):
    output = ""
    if i % x == 0:
        output += "Fizz"
    if i % y == 0:
        output += "Buzz"
    if output == "":
        output = i
    print(output)
