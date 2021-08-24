import sys

def is_special(letter):
    return 33 <= ord(letter) <= 42 or 91 <= ord(letter) <= 93
def add_backslash(line):
    result = []
    for letter in line:
        if is_special(letter):
            result.append('\\')
        result.append(letter)
    return ''.join(result)


#lines = sys.stdin.readlines()
# for i in range(0, len(lines), 2):
#     n = int(lines[i].strip())
#     line = lines[i + 1].strip()
#     for _ in range(n):
#         line = add_backslash(line)
#     print(line)

try:
    while True:
        n = int(input())
        line = input()
        for i in range(n):
            line = add_backslash(line)
        print(line)
except EOFError:
    pass
