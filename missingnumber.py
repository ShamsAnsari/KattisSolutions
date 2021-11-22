'''
:( :( :( works tho
'''

def convert(nums_str):
    nums = []
    i = 0
    incr = 1
    curr_index = 0
    while i < len(nums_str):
        if i == 8:
            incr += 1
            if nums_str[i] == '9':
                curr_index += 1
                nums.append(9)
                i += 1
                continue
        if curr_index == 98:
            incr += 1
            if nums_str[i] == '1':
                nums.append(100)
                break

    

        
        nums.append(int(nums_str[i:i + incr]))
        i += incr
        curr_index += 1
    return nums

    

num_nums = int(input())
nums_str = input()
nums = convert(nums_str)

if num_nums == 100 and nums_str[-1] != '0':
    print(100)
    exit(0)

if 100 > num_nums > 9 and int(nums_str[len(nums_str)-2:]) != num_nums:
    print(num_nums)
    exit(0)

if num_nums < 10 and int(nums_str[len(nums_str)-1:]) != num_nums:
    print(num_nums)
    exit(0)

#print(nums)


for i in range(len(nums)):
    if nums[i] != i + 1:
        print(i + 1)
        break

''''
100
1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374757677787980818283848586878889909192939495969798100

2
1
'''