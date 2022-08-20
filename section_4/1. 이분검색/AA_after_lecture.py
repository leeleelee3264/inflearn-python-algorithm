import sys

sys.stdin = open('in5.txt', 'rt')
n, m = map(int, input().split())
nums = list(map(int, input().split()))

# binary search 를 통해서 검색
nums.sort()
idx = 0

lt = 0
rt = n - 1

# for 문으로 돌릴 수 있었던 거 같은데 while 로 하는 게 편한듯
while lt <= rt:
    mid = (lt + rt) // 2

    if nums[mid] == m:
        idx = mid
        break
    elif nums[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1


print(idx + 1)


print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())

