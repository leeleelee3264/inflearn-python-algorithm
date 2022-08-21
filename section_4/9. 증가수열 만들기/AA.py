import sys

sys.stdin = open('in5.txt', 'rt')
n = int(input())
nums = list(map(int, input().split()))


lt = 0
rt = n - 1
direction = ''
prev_num = 0

while lt <= rt:
    if nums[lt] <= prev_num and nums[rt] <= prev_num:
        break

    if nums[lt] > prev_num and nums[rt] > prev_num:
        if nums[lt] <= nums[rt]:
            direction = direction + 'L'
            prev_num = nums[lt]
            lt = lt + 1
        elif nums[lt] > nums[rt]:
            direction = direction + 'R'
            prev_num = nums[rt]
            rt = rt - 1
    elif nums[lt] > prev_num:
        direction = direction + 'L'
        prev_num = nums[lt]
        lt = lt + 1
    else:
        direction = direction + 'R'
        prev_num = nums[rt]
        rt = rt - 1


print(len(direction))
print(direction)
print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
print(input())

