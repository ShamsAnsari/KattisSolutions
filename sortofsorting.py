out = ""
while True:
    n = int(input())
    if n == 0:
        break
    names = []
    for i in range(n):
        names.append(input())
    names = sorted(names, key=lambda name: name[0:2])

    for name in names:
        out += name + "\n"
    out += "\n"
print(out[0:len(out) - 2])
