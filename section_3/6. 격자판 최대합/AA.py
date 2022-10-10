import sys

sys.stdin = open('in5.txt', 'rt')
n = int(input())


def _sum_diagonal_primary(lst):
    sums = 0
    for i in range(len(lst)):
        sums = sums + lst[i][i]

    return sums


def _sum_diagonal_secondary(lst):
    sums = 0
    for i in range(len(lst)):
        sums = sums + lst[i][len(lst) - i - 1]

    return sums


nums = []

for i in range(n):
    a = list(map(int, input().split()))
    nums.append(a)

results = []

# 각 행
for i in range(n):
    results.append(sum(nums[i]))

# 각 열
changed_dem = list(map(list, zip(*nums)))
for i in range(n):
    results.append(sum(changed_dem[i]))

# 대각선
results.append(_sum_diagonal_primary(nums))
results.append(_sum_diagonal_secondary(nums))

print(max(results))

print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
