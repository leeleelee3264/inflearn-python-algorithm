import sys

sys.stdin = open('in1.txt', 'rt')
n = int(input())

a = []

for i in range(n):
    _ = list(map(int, input().split()))
    a.append(_)

# padding zero to 2d array
a.insert(0, [0]*n)
a.append([0]*n)

for x in a:
    x.insert(0, 0)
    x.append(0)

count = 0

# 위아래 왼쪽 오른쪽 순회 하는 방법
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n+1):
    for j in range(1, n+1):
        # all: 모두가 참이어야 한다.
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            count+=1

print(count)
print('-----')
print('-----')
sys.stdin = open('out1.txt', 'rt')
print(input())

