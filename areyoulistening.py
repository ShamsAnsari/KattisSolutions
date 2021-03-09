import math
"""
Not Completed/Not submitted
"""
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def intersects(device1, device2):
    x1, y1, r1 = device1
    x2, y2, r2  = device2
    dist_devices = distance([x1, y1], [x2, y2])
    return dist_devices <= r1 + r2

def intersects_3(my_device, listening_devices):
    num_intersects = 0
    for listening_device in listening_devices:
        if intersects(my_device, listening_device):
            num_intersects += 1
            if num_intersects >= 3:
                return True
    return False


cx, cy, n = map(int, input().split())

listening_devices = []
for i in range(n):
    x, y, r = map(int, input().split())
    listening_devices.append([x,y,r])




my_device = [cx,cy,0]
while not intersects_3(my_device,listening_devices):
        my_device[2] += 1

if my_device[2] == 0:
    print(0)
else:
    print(my_device[2]-1)
