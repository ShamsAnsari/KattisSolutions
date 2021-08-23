class Union_Find:
    def __init__(self, n):
        self.n = n
        self.parents = [None]
        self.counts = [None]
        self.total_sum =[None]

        for i in range(1, n + 1):

            self.parents.append(i)
            self.counts.append(1)
            self.total_sum.append(i)

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        self.counts[self.find(y)] += self.counts[self.find(x)]
        self.total_sum[self.find(y)] += self.total_sum[self.find(x)]
        self.parents[self.find(x)] = self.find(y)

    def move(self, x, y):



    def count(self, x):
        return self.counts[self.find(x)]

    def total(self, x):
        return self.total_sum[self.find(x)]


try:
    while True:
        line = input()
        if line == "":
            break
        num_ints, num_commands = map(int, line.split())
        union_find = Union_Find(num_ints)

        for i in range(num_commands):
            data = list(map(int, input().split()))
            if data[0] == 1:
                union_find.union(data[1],data[2])
            elif data[0] == 2:
                union_find.move(data[1], data[2])
            elif data[0] == 3:
                #print("output=",end="")
                print(union_find.count(data[1]), union_find.total(data[1]))
                # print("Parents: {}".format(union_find.parents))
                # print("Counts: {}".format(union_find.counts))
                # print("total_sum: {}".format(union_find.total_sum))


except EOFError:
    pass
