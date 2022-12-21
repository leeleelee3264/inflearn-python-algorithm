import sys
from collections import deque

sys.stdin = open('in5.txt', 'rt')

S = input()
N = int(input())

SS = []

for i in range(N):
    SS.append(input())

for i in range(N):
    _S = deque([ch for ch in S])
    q = deque([ch for ch in SS[i]])
    res = []
    idx = 0
    flag = False

    for j in q:

        if j == S[idx] and not res.__contains__(j):
            res.append(j)
            _S.popleft()
            idx+=1
            if idx == len(S):
                break
        elif j in _S:
            flag = True
            break

    r = ''.join(res)
    if flag:
        print(f'#{i+1} NO')
    elif r == S:
        print(f'#{i+1} YES')
    else:
        print(f'#{i+1} NO')


print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')

for i in range(N):
    a = input()
    print(a)
