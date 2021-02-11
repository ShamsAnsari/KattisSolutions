def digit_counts(num):
    counts = [0] * 10
    list_num = [int(x) for x in str(num)]
    for num in list_num:
        counts[num] += 1
    return counts


def is_creeper(num):
    digitCounts = digit_counts(num)
    if (digitCounts[1] == 1) and (digitCounts[2] == 1) and (digitCounts[3] >= 2) and (digitCounts[4] == 4) and (
            digitCounts[5] == 0) and (digitCounts[6] == 0) and (digitCounts[7] == 0) and (digitCounts[8] == 0) and (
            digitCounts[9] == 0):
        return True

    if (digitCounts[1] == 0) and (digitCounts[2] == 0) and (digitCounts[3] == 0) and (digitCounts[4] == 0) and (
            digitCounts[5] == 2) and (digitCounts[6] >= 2) and (digitCounts[7] == 4) and (digitCounts[8] == 0) and (
            digitCounts[9] == 0):
        return True

    return False


def sort_num(num):
    list_num = [int(x) for x in str(num)]
    list_num.sort()
    for num in list_num:
        if num > 0:
            break
        list_num.pop(0)
    return int(''.join(map(str, list_num)))


def reverse(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num


def rat(num, m, k):
    rats = []
    for i in range(1,m + 1):

        if is_creeper(num):
            print(k, "C", i)
            return

        if num in rats:
            print(k, "R", i)
            return

        rats.append(num)
        rev_num = reverse(num)
        num += rev_num
        num = sort_num(num)

    print(k, rats[-1])


p = int(input())

while p > 0:
    k, m, init_val = map(int, input().split())
    rat(init_val, m, k)
    p -= 1
