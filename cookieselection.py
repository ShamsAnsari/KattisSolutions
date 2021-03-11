from sys import stdin
from queue import PriorityQueue

class MaxQueue():
    def __init__(self):
        self.max_queue = PriorityQueue()
    def put(self, num):
        self.max_queue.put(-num)
    def get(self):
        return -self.max_queue.get()
    def __len__(self):
        return len(self.max_queue)

min_queue = PriorityQueue()
max_queue = MaxQueue()

for line in stdin:
    line = line.strip()
    if line == "":
        break
    if line == "#":
        cookie = min_queue.get()
        if len(max_queue) != len(min_queue):
            min_queue.put(max_queue.get())
    else:
        queue.add(int(line))
