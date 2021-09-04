class Node:
    def __init__(self, pos):
        assert type(pos) == tuple, "pos must be a tuple"
        self.pos = pos # (A, 1) format

    def neighbors(self):
        int_pos0 = ord(self.pos[0])

        top_right = Node((chr(int_pos0 + 1), self.pos[1] + 1))
        top_left = Node((chr(int_pos0 - 1), self.pos[1] + 1))
        bottom_right = Node((chr(int_pos0 + 1), self.pos[1] - 1))
        bottom_left = Node((chr(int_pos0 - 1), self.pos[1] - 1))

        possible = [top_right, bottom_right, bottom_left, top_left]
        neighbors = []
        for p_neigh in possible:
            if p_neigh.inbounds():
                neighbors.append(p_neigh)

        return neighbors

    def inbounds(self):
        return 'A' <= self.pos[0] <= 'H' and 1 <= self.pos[1] <= 8

    def path(self, target):

        queue = [self]
        came_from = {}
        came_from[self] = None
        found = False
        while queue:
            curr = queue.pop(0)
            if curr == target:
                found = True
                break
            for neighbor in curr.neighbors():
                if neighbor not in came_from:
                    queue.append(neighbor)
                    came_from[neighbor] = curr

        if not found:
            return []

        curr = target
        path = []
        while curr != self:
            path.append(curr)
            curr = came_from[curr]
        path.append(self)
        path.reverse()
        return path

    def __repr__(self):
        return f"({self.pos[0]}, {self.pos[1]})"

    def __str__(self):
        return self.__repr__()


    def __eq__(self, other):
        if isinstance(other, Node):
            return self.__key__() == other.__key__()
        return NotImplemented

    def __key__(self):
        return self.pos

    def __hash__(self):
        return hash(self.__key__())

num_tests = int(input())

for _ in range(num_tests):
    x1, y1, x2, y2 = input().split()
    start = Node((x1, int(y1)))
    target = Node((x2, int(y2)))
    path = start.path(target)
    print(path)
