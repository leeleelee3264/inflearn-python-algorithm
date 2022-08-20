import sys


sys.stdin = open('in6.txt', 'rt')
n, m = map(int, input().split())
nums = list(map(int, input().split()))

lt = max(nums)
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

    if counter <= m:
        rt = mid - 1
        results.append(mid)
    else:
        lt = mid + 1

print(min(results))

print('-----')
print('-----')
sys.stdin = open('out6.txt', 'rt')
print(input())

