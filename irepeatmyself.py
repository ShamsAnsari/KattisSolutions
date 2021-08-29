def check_repeating(string, substring):
    num_fit = len(string) // len(substring)
    for i in range(num_fit):
        a = i * len(substring)
        b = a + len(substring)
        if substring != string[a:b]:
            return False

    remainder = len(string) % len(substring)
    if remainder == 0:
        return True
    else:
        return string[-remainder:] == substring[:remainder]

num_tests = int(input())
for _ in range(num_tests):
    line = input()
    n = len(line)
    for i in range(1,n + 1):
        if check_repeating(line, line[:i]):
            print(i)
            break
