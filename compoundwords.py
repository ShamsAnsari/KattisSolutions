
words = []
compoundWords = set()

try:
    while True:
        inp = input()
        if inp == "":
            break
        words.extend(inp.strip().split(" "))
except EOFError:
    pass

for i in range(len(words)):
    for j in range(len(words)):
        if i == j:
            continue
        compoundWords.add(words[i] + words[j])

sortedWords = sorted(compoundWords)

for word in sortedWords:
    print(word)


