import sys


sys.stdin = open('in5.txt', 'rt')
n, k = map(int, input().split())

answer = -1
counter = 0

for i in range(1, n + 1):
    if n % i == 0:
        counter = counter + 1

    if counter == k:
        answer = i
        break
else:
    answer = -1

sys.stdin = open('out5.txt', 'rt')
out_args = input()

print(f'my answer is {answer}')
print(f'output answer is {out_args}')
