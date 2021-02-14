while True:
    max_width = int(input())
    if max_width == 0:
        break
    data = []
    while True:
        width, height = map(int, input().split())
        if width == -1 and height == -1:
            break
        data.append([width, height])

    max_used_width = 0
    total_height = 0
    level_height = 0
    curr_width = 0
    for rectangle in data:
        width, height = rectangle
        if curr_width + width > max_width:
            level_height = total_height
            curr_width = 0
        if level_height + height > total_height:
            total_height = level_height + height
        curr_width += width
        if curr_width > max_used_width:
            max_used_width = curr_width

    print(max_used_width, "x", total_height)
