import sys

sys.stdin = open('in5.txt', 'rt')
n = int(input())

a = []

for i in range(n):
    _ = list(map(int, input().split()))
    a.append(_)

count = 0

for i in range(0, n):
    for j in range(0, n):
        target = a[i][j]

        top = a[i-1][j] if i-1 >=0 else 0
        down = a[i+1][j] if i+1<n else 0
        left = a[i][j-1] if j-1 >=0 else 0
        right = a[i][j+1] if j+1<n else 0
        if target > top and target > down and target > left and target > right:
            count+=1


print(count)
print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())

