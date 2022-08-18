# K 번째 수
import sys

sys.stdin = open('in5.txt', 'rt')

T = int(input())

for i in range(T):
    n, s, e, k = map(int, input().split())
    nums = [int(j) for j in input().split()]

    target_nums = nums[s-1:e]
    target_nums.sort()
    answer = target_nums[k-1]

    print(f'#{i+1} {answer}')


print('---------')
print('---------')

sys.stdin = open('out5.txt', 'rt')
for i in range(T):
    print(input())
