import sys


sys.stdin = open('in5.txt', 'rt')
n, c = map(int, input().split())

vector = []


def _counter(mid, c, vectors):
    counter = 1
    prev = 0
    idx = 1

    while idx < c:
        for j in range(prev + 1, len(vectors)):
            if vector[j] - vector[prev] >= mid:
                counter = counter + 1
                prev = j
        idx = idx + 1

    return counter


for i in range(n):
    vector.append(int(input()))

vector.sort()

# 가장 가까운 말들이
# 최대로 먼 거리에 있도록

lt = min(vector)
rt = max(vector)
results = []

while lt <= rt:
    # 가까운 거리에 있던 먼 거리에 있던 최소 5를 넘어야 한다.
    mid = (lt + rt) // 2
    counter = _counter(mid, c, vector)

    if counter >= c:
        lt = mid + 1
        results.append(mid)
    else:
        rt = mid - 1


print(max(results))

print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())



