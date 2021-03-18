from sys import stdin

def print_graph(graph):
    for i in range(len(graph)):
        print("Node: {} Neighbors: {}".format(i,graph[i]))


def distance(p1, p2):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    return abs(x1-x2) + abs(y1-y2)


def create_graph(nodes):
    num_nodes = len(nodes)
    graph = [None] * num_nodes
    for i in range(num_nodes):
        graph[i] = []
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and distance(nodes[i], nodes[j]) <= 1000:
                graph[i].append(j)
    return graph

def BFS(graph, start, goal):
    num_nodes = len(graph)
    queue = []
    visited = [False] * num_nodes

    queue.append(start)


    while queue:
        node = queue.pop(0)
        visited[node] = True
        if node == goal:
            return True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)

    return False


for i in range(int(stdin.readline().rstrip())):
    n = int(stdin.readline().rstrip())
    nodes = []

    start = list(map(int, stdin.readline().rstrip().split()))
    nodes.append(start)

    for i in range(n):
        store = list(map(int, stdin.readline().rstrip().split()))
        nodes.append(store)

    end = list(map(int, stdin.readline().rstrip().split()))
    nodes.append(end)


    graph = create_graph(nodes)
    print("happy") if BFS(graph, len(nodes) - 1, 0) else print("sad")
