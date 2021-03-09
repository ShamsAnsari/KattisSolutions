import sys
try:
    def solve(n):
        stack = []
        queue = []
        priority_queue = []
        type_ds = [True, True, True]
        for i in range(n):
            command, element = map(int, input().split())
            if command == 1:
                if type_ds[0] != False:
                    stack.append(element)
                if type_ds[1] != False:
                    queue.append(element)
                if type_ds[2] != False:
                    priority_queue.append(element)
            elif command == 2:
                if type_ds[0] != False:
                    if len(stack) == 0:
                        return "impossible"
                    if element != stack.pop():
                        type_ds[0] = False
                        stack.clear()
                if type_ds[1] != False:
                    if len(queue) == 0:
                        return "impossible"
                    if element != queue.pop(0):
                        type_ds[1] = False
                        queue.clear()
                if type_ds[2] != False:
                    if len(priority_queue) == 0:
                        return "impossible"
                    priority_queue.sort(reverse=True)
                    if element != priority_queue.pop(0):
                        type_ds[2] = False
                        priority_queue.clear()


        if type_ds.count(True) > 1:
            return "not sure"
        elif type_ds.count(True) == 0:
            return "impossible"
        else:
            if type_ds[0] == True:
                return "stack"
            elif type_ds[1] == True:
                return "queue"
            else:
                return "priority queue"

    for line in sys.stdin:
        if line.strip() == "":
            break
        n = int(line.strip())
        print(solve(n))
except:
    pass
