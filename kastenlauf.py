
class Union_Find:
    def __init__(self, num_nodes):
        self.parents = []
        for i in range(num_nodes):
            self.parents.append(i)

    def union(self, x, y):
        self.parents[x] = self.find(y)

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

def distance(p1, p2):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    return abs(x1-x2) + abs(y1-y2)


for i in range(int(input())):
    n = int(input())
    nodes = []

    start = list(map(int, input().split()))
    nodes.append(start)

    for i in range(n):
        store = list(map(int, input().split()))
        nodes.append(store)

    end = list(map(int, input().split()))
    nodes.append(end)

    num_nodes = len(nodes)

    union_find = Union_Find(num_nodes)
    for i in range(num_nodes):
        for j in range(num_nodes):
            if (i != j and distance(nodes[i], nodes[j]) <= 1000
            and union_find.find(i) != union_find.find(j)):
                    union_find.union(i,j)
    print("happy") if union_find.find(0) == union_find.find(num_nodes - 1) else print("sad")
