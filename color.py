num_socks, capacity, max_diff = map(int, input().split())
socks = list(map(int, input().split()))
socks.sort()

num_machines = 1
curr_capacity = 1
for i in range(1, num_socks):
    if abs(socks[i] - socks[i - 1]) > max_diff or curr_capacity >= capacity:
        num_machines += 1
        curr_capacity = 0

    curr_capacity += 1


print(num_machines)
