# K번째 큰 수
import sys

sys.stdin = open('in5.txt', 'rt')
n, k = map(int, input().split())

cards = list(map(int, input().split()))

result = set()

for i in range(n):
    for j in range(i+1, n):
        for z in range(j+1, n):
            sum = cards[i] + cards[j] + cards[z]
            result.add(sum)


sorted_result = sorted(result, reverse=True)
print(sorted_result[k-1])


print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
