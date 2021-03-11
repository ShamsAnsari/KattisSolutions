from sys import stdin
import heapq
"""
maxh|minh
----|----
|1|2|3|4| len = 4
-------------------
|0|1|2|3| median = arr[2] = 3 or minh[0]
"""

import heapq
"""
maxh|minh
----|------
|1|2|3|4|5| len = 5
-------------------
|0|1|2|3|4| median = arr[2] = 3 or or minh[0]
"""

class MaxHeap():
    def __init__(self):
        self.max_heap = []

    def push(self, element):
        heapq.heappush(self.max_heap, -element)

    def pop(self):
        return -heapq.heappop(self.max_heap)

    def peek(self):
        return -self.max_heap[0]

    def __len__(self):
        return len(self.max_heap)

    def __str__(self):
        return str(self.max_heap)

    def __repr__(self):
        return str(self.max_heap)


min_heap = []
max_heap = MaxHeap()

for line in stdin:
    line = line.strip()
    #print(max_heap, min_heap)
    if line == "":
        break
    if line == "#":
        if len(min_heap) > 0:
            cookie = heapq.heappop(min_heap)
            print(cookie)
            if len(max_heap) > len(min_heap):
                heapq.heappush(min_heap, max_heap.pop())
    else:
        cookie = int(line)
        if len(min_heap) > 0 and cookie < min_heap[0]:
            max_heap.push(cookie)
        else:
            heapq.heappush(min_heap, cookie)

        if len(min_heap) - len(max_heap) > 1:
            max_heap.push(heapq.heappop(min_heap))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, max_heap.pop())
