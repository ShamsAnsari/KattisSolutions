def is_arithmetic(nums):
    diff = nums[1] - nums[0]
    for j in range(1, len(nums)):
        if nums[j] - nums[j - 1] != diff:
            return False
    return True


n = int(input())

for i in range(n):
    nums = list(map(int, input().split()))
    nums.pop(0)

    if is_arithmetic(nums):
        print("arithmetic")
    else:
        if is_arithmetic(sorted(nums)):
            print("permuted arithmetic")
        else:
            print("non-arithmetic")
