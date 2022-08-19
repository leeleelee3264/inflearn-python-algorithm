import sys

sys.stdin = open('in5.txt', 'rt')
n = int(input())
nums = list(map(int, input().split()))

possible_results = [0 for i in range(n)]

for index in range(len(nums)):
    num_list = list(map(int, str(nums[index])))
    sums = sum(num_list)
    possible_results[index] = sums

maxs = max(possible_results)
index = possible_results.index(maxs)

print(nums[index])

print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
