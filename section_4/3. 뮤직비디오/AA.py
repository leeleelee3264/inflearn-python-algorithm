import sys


sys.stdin = open('in5.txt', 'rt')
n, m = map(int, input().split())
nums = list(map(int, input().split()))

lt = 1
rt = sum(nums)
results = []


def _counter(mid):
    cnt = 1
    sum = 0

    for x in nums:
        if sum + x > mid:
            cnt = cnt + 1
            sum = x
        else:
            sum = sum + x

    return cnt


while lt <= rt:
    mid = (lt + rt) // 2

    counter = _counter(mid)

    if counter > m:
        lt = mid + 1
    elif counter <= m:
        rt = mid - 1
        results.append(mid)

print(min(results))

print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())

