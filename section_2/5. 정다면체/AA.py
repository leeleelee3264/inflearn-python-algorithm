import sys

sys.stdin = open('in5.txt', 'rt')
n, m = map(int, input().split())

possible_results = [0 for i in range(n + m)]

# 주사위의 모든 확률을 구한다
for i in range(1, n+1):
    for j in range(1, m+1):
        sum = i + j
        possible_results[sum-1] += 1

max_result = max(possible_results)

for index in range(len(possible_results)):
    if possible_results[index] == max_result:
        print(index + 1, end=' ')

print()
print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
