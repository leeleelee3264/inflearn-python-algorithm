import sys


sys.stdin = open('in5.txt', 'rt')
n, c = map(int, input().split())

vector = []


def _counter(mid, vectors):
    counter = 1
    prev = 0

    # 주어진 말을 다 배치하는 것은 중요하지 않다.
    # 더 많은 말을 배치해도 되고, 더 적은 말을 배치해도 된다.
    # 여기는 그냥 몇마리 배치가 되나가 중요하니 꼭 이중 for 돌면서 다 배치 안 해도 된다.
    for j in range(prev + 1, len(vectors)):
        if vector[j] - vector[prev] >= mid:
            counter = counter + 1
            prev = j

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
    counter = _counter(mid, vector)

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



