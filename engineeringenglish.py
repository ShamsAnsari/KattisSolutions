try:
    repeated = []
    while True:
        line = input().strip()
        if line == "":
            break
        words = line.split()
        for i in range(len(words)):
            if words[i].lower() in repeated:
                words[i] = "."
            else:
                repeated.append(words[i].lower())
        print(' '.join(words))
except EOFError:
    pass
