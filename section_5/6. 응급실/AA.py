import sys
from collections import deque

sys.stdin = open('in5.txt', 'rt')
N, M = map(int, input().split())
nums = list(map(int, input().split()))

q = deque()

# -1로 내가 표시한 게 뭔지를 아는 게 어떨까 위급도로 음수가 나오지는 않겠지
for i in range(len(nums)):
    if i == M:
        q.append(nums[i]*-1)
    else:
        q.append(nums[i])

counter = 0

while True:
    m = max(q, key=abs)
    if q[0] == m:
        counter+=1
        if q[0] < 0:
            break
        q.popleft()
    else:
        q.rotate(-1)



print(counter)
print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
a = input()
print(a)
