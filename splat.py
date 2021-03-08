import math
def get_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def get_color(x,y):
    for paint_drop in paint_drops:
        drop_x, drop_y, vol, color = paint_drop
        radius = math.sqrt(vol/math.pi)
        # Kattis still on python 3.6,  math.dist() available in 3.8
        #distance = math.dist([x,y], [drop_x, drop_y])
        distance = get_distance([x,y], [drop_x, drop_y])
        if distance <= radius:
            return color
    return "white"

num_paint_descriptions = int(input())
while num_paint_descriptions > 0:
    num_paint_drops = int(input())
    paint_drops = []
    for i in range(num_paint_drops):
        x,y, vol, color = input().split()
        x, y, vol = float(x), float(y), float(vol)
        paint_drops.insert(0,[x,y,vol,color])

    num_queries = int(input())
    for i in range(num_queries):
        query = map(float, input().split())
        color = get_color(*query)
        print(color)
    num_paint_descriptions -= 1
