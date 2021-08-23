
# C = # of words
# R = length of word
result = ""
while True:
    r, c = map(int, input().split())
    if r == 0 and c == 0:
        break

    words = ["" for _ in range(c)]
    for _ in range(r):
        string = input()
        for i in range(c):
            words[i] += string[i]
    words.sort(key = lambda l: l.lower())

    for i in range(r):
        for j in range(c):
            result += words[j][i]
        result += "\n"
    result += "\n"
print(result[:-1], end= "")
