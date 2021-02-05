"""
Kattis:  Time exceeded
Solution has correct approach but python is way too slow for this problem

MUST solve this problem in c++ only.

C++ solution accepted

"""

import math

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, u, v):
        x = self.find(parent, u)
        y = self.find(parent, v)

        parent[x] = y


    def kruskal(self):

        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []

        for node in range(self.V):
            parent.append(node)


        total_distance = 0.0
        i = 0
        while i < self.V - 1:
            u, v, w = self.graph.pop(0)
            u_parent = self.find(parent, u)
            v_parent = self.find(parent, v)
            if u_parent != v_parent:
                i += 1
                total_distance += w
                self.union(parent,u, v)

        return total_distance


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def calculate(data):
    V = len(data)
    graph = Graph(V)
    for i in range(V):
        for j in range(i + 1, V):
            graph.add_edge(i, j, distance(data[i], data[j]))

    return graph.kruskal()


T = int(input())
while T > 0:
    M = int(input())
    data = []
    while M > 0:
        x, y = [float(data) for data in input().rstrip().split(" ")]
        data.append([x, y])
        M -= 1
    print(calculate(data))
    T -= 1
