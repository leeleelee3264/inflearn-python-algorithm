import sys
from collections import deque


sys.stdin = open('in5.txt', 'rt')
n = int(input())

a = []

for i in range(n):
    _ = list(map(int, input().split()))
    a.append(_)

m = int(input())
o = []

for i in range(m):
    _ = list(map(int, input().split()))
    o.append(_)


# 회전 연산
for i in range(m):
    row, direction, rotate = o[i][0] - 1, o[i][1], o[i][2]
    items = deque(a[row])

    if direction == 0: # 왼쪽
        items.rotate(-1 * rotate)
    else: # 오른쪽
        items.rotate(rotate)

    a[row] = list(items)


# 값 더하기
res = 0
mid = n // 2
start = 0
end = n

for i in range(n):
    for j in range(start, end):
        res += a[i][j]

    if i < mid:
        start = start + 1
        end = end - 1
    else:
        start = start - 1
        end = end + 1



print(res)
print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())


