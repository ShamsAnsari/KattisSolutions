class Box:
    def __init__(self, x1, y1, x2, y2, size):
        self.x1 = float(x1)
        self.x2 = float(x2)
        self.y1 = float(y1)
        self.y2 = float(y2)
        self.size = size

    def overlap(self, x, y):
        return self.x2 >= x >= self.x1 and self.y2 >= y >= self.y1

    def __str__(self):
        return str(self.x1) + " " + str(self.x2) + " " + str(self.y1) + " " + str(self.y2) + " " + str(self.size)

    def __repr__(self):
        return str(self)


def find_package(peanut, boxes):
    for box in boxes:
        if box.overlap(float(peanut[0]), float(peanut[1])):
            if box.size == peanut[2]:
                return "correct"
            else:
                return box.size
    return "floor"


try:
    while True:
        n = int(input())
        if n == 0:
            break
        boxes = []
        while n > 0:
            line = input().rstrip().split()
            boxes.append(Box(*line))
            n -= 1
        m = int(input())
        while m > 0:
            peanut = input().rstrip().split()
            package = find_package(peanut, boxes)
            print(peanut[2] + " " + package)
            m -= 1
        print()
except EOFError:
    pass
