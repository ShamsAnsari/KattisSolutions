class Union_Find():
    def __init__(self, people):
        self.network_size = {}
        self.parents = {}
        # init parents and  network size
        for person in people:
            self.parents[person] = person
            self.network_size[person] = 1

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        self.network_size[self.find(y)] += self.network_size[self.find(x)]
        self.parents[self.find(x)] = self.find(y)



for t in range(int(input())):

    data = []
    people = set()

    f = int(input())
    for i in range(f):
        x, y = input().split()
        people.add(x)
        people.add(y)
        data.append([x,y])

    network = Union_Find(people)

    for x, y in data:
        if network.find(x) != network.find(y):
            network.union(x, y)
        print(network.network_size[network.find(y)])
