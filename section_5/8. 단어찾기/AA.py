import sys
from collections import deque

sys.stdin = open('in4.txt', 'rt')

N = int(input())

d = {}
for i in range(N):
    d[input()] = 0

for i in range(N-1):
    d[input()]+=1

for key in d.keys():
    if d[key] == 0:
        print(key)
        break



print('-----')
print('-----')
sys.stdin = open('out4.txt', 'rt')

a = input()
print(a)
