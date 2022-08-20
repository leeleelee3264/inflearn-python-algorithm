import sys

sys.stdin = open('in5.txt', 'rt')
n, m = map(int, input().split())
nums = list(map(int, input().split()))

sorted_nums = nums.sort()
idx = nums.index(m) + 1

print(idx)


print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
