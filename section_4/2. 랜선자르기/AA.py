import sys


sys.stdin = open('in5.txt', 'rt')
n, k = map(int, input().split())
nums = []
lengths = []

for i in range(n):
    nums.append(int(input()))

nums.sort()

lt = 0
rt = max(nums)

while lt <= rt:
    mid = (lt + rt) // 2
    counter = 0

    for num in nums:
        counter = counter + (num // mid)

    if counter < k:
        rt = mid - 1

    if counter >= k:
        lengths.append(mid)
        lt = mid + 1

print(max(lengths))

print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
