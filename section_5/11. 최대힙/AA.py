import sys
import heapq

sys.stdin = open('in5.txt', 'rt')

h = []
res = []
while True:
    N = int(input())
    if N == -1:
         break

    if N == 0:
        res.append(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (N*-1, N))

print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')

aa = []
try:
    while True:
        a = int(input())
        aa.append(a)
except EOFError:
    pass


if aa == res:
    print('Correct')