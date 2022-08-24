import sys

sys.stdin = open('in5.txt', 'rt')
n, m = map(int, input().split())
nums = list(map(int, input().split()))

results = []

for i in range(n):
    end = i + 1
    sums = nums[i]
    results.append(sums)

    while end < n:
        if sums > m or m < nums[end]:
            break

        sums = sums + nums[end]
        end = end + 1
        results.append(sums)


print(results.count(m))


print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
