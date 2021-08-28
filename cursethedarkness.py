import math

get_x = lambda loc: loc[0]
get_y = lambda loc: loc[1]

def distance(a, b):
    return math.sqrt((get_x(a) - get_x(b)) ** 2 + (get_y(a) - get_y(b)) ** 2 )


num_tests = int(input())


for _ in range(num_tests):
    book = list(map(float, input().split()))
    num_candles = int(input())
    candles = []
    for _ in range(num_candles):
        x, y = map(float, input().split())
        candles.append([x, y])

    found = False
    for candle in candles:
        if distance(book, candle) <= 8:
            found = True
            break
    print("light a candle" if found else "curse the darkness")
