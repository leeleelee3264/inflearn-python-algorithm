import sys
from collections import deque

sys.stdin = open('in5.txt', 'rt')
n, k = map(int, input().split())

q = deque()

# 큐에 다 넣어주기
for i in range(n):
    q.append(i+1)


# 큐에 하나 남기 전까지 rotate 해주기
# idx가 2가 되면 맨 앞을 pop 하면 된다.

counter = 0
while len(q)!=1:
    if counter == k-1:
        q.popleft()
        counter = 0
        continue
    q.rotate(-1)
    counter+=1

print(q[0])

print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
a = input()
print(a)
