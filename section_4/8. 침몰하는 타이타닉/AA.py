import sys

sys.stdin = open('in5.txt', 'rt')
n, m = map(int, input().split())
weights = list(map(int, input().split()))


weights.sort()

counter = 0

for i in range(n):
    if weights[i] == 0:
        continue
    this_weight = weights[i]
    counter = counter + 1
    for j in range(n-1, 0, -1):
        if weights[j] == 0:
            continue
        if this_weight + weights[j] <= m:
            weights[j] = 0
            weights[i] = 0
            break


print(counter)
print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
