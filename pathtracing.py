def inBounds(rows, cols, r, c):
    return r >= 0 and c >= 0 and c < cols and r < rows


def printMap(map):
    rows = len(map)
    cols = len(map[0])
    print("#" * (cols + 2))
    for r in range(rows):
        print("#", end="")
        for c in range(cols):
            print(map[r][c], end="")
        print("#")
    print("#" * (cols + 2))


def calculateBound(data):
    ub = db = rb = lb = 0
    x = y = 0

    for datum in data:
        if datum == "up":
            y += 1
            if y > ub:
                ub += 1
        elif datum == "down":
            y -= 1
            if y < db:
                db -= 1
        elif datum == "right":
            x += 1
            if x > rb:
                rb += 1
        elif datum == "left":
            x -= 1
            if x < lb:
                lb -= 1

    return ub - db + 1, -lb + rb + 1


def shiftMap(map, shift):
    rows = len(map)
    cols = len(map[0])

    shifted_map = [None] * rows
    for r in range(rows):
        shifted_map[r] = [" "] * cols

    dr, dc = 0, 0
    br, bc = [0, 0], [0, 0]

    if shift == "up":
        dr = 1
        br = [0, -1]
    elif shift == "down":
        dr = -1
        br = [1, 0]
    elif shift == "right":
        dc = -1
        bc = [1, 0]
    elif shift == "left":
        dc = 1
        bc = [0, -1]

    for r in range(br[0], rows + br[1]):
        for c in range(bc[0], cols + bc[1]):
            shifted_map[r][c] = map[r + dr][c + dc]
    return shifted_map


data = []
try:
    while True:
        line = input()
        if line == "":
            break
        datum = line.rstrip()
        data.append(datum)
except EOFError:
    pass

rows, cols = calculateBound(data)
map = [None] * rows
for r in range(rows):
    map[r] = [" "] * cols

map[0][0] = "S"
r = c = 0
for datum in data:
    if datum == "up":
        if inBounds(rows, cols, r - 1, c):
            r -= 1
        else:
            map = shiftMap(map, "down")
    elif datum == "down":
        if inBounds(rows, cols, r + 1, c):
            r += 1
        else:
            map = shiftMap(map, "up")
    elif datum == "right":
        if inBounds(rows, cols, r, c + 1):
            c += 1
        else:
            map = shiftMap(map, "left")
    elif datum == "left":
        if inBounds(rows, cols, r, c - 1):
            c -= 1
        else:
            map = shiftMap(map, "right")
    if map[r][c] == " ":
        map[r][c] = "*"
map[r][c] = "E"
printMap(map)
