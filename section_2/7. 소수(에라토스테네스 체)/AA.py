import sys

sys.stdin = open('in3.txt', 'rt')
n = int(input())

nums = [0 for i in range(n + 1)]
cnt = 0

for i in range(2, n + 1):
    if nums[i] == 0:
        cnt = cnt + 1
        for j in range(i + 1, n + 1):
            if j % i == 0:
                nums[j] = -1

print(cnt)

print('-----')
print('-----')
sys.stdin = open('out3.txt', 'rt')
print(input())
