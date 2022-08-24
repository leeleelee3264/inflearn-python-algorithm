import sys

sys.stdin = open('in1.txt', 'rt')
n = int(input())


def _print_diagonal(lst):
    # To print Primary Diagonal
    print('Diagonal 1 - ', end="")
    print([lst[i][i] for i in range(len(lst))])

    # To print Secondary Diagonal
    print('Diagonal 2 - ', end="")
    print([lst[i][len(lst) - i - 1] for i in range(len(lst))])


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

