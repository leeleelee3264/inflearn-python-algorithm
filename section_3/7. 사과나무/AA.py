import sys


sys.stdin = open('in5.txt', 'rt')
n = int(input())

a = []

for i in range(n):
    _ = list(map(int, input().split()))
    a.append(_)

res = 0
start = end = n // 2

for i in range(n):
    for j in range(start, end+1):
        res += a[i][j]

    if i < n // 2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1


print(res)
print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())


