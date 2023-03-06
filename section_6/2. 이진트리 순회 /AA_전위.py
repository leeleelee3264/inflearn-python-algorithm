import heapq

h = []
heapq.heappush(h, 1)
heapq.heappush(h, 2)
heapq.heappush(h, 3)
heapq.heappush(h, 4)
heapq.heappush(h, 5)
heapq.heappush(h, 6)
heapq.heappush(h, 7)


# 전위순위 출력
# 방문 순서
# 왼쪽을 돌고 오른쪽을 돈다.
def DFS(idx):
    if idx >= len(h):
        return
    print(h[idx])
    # left
    DFS(idx * 2 + 1)
    # right
    DFS(idx * 2 + 2)

DFS(0)