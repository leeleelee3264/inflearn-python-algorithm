import sys

sys.stdin = open('in5.txt', 'rt')

N = list(input())
K = list(input())

N_d = {}
K_d = {}

for n in N:
    N_d.setdefault(n, 0)
    N_d[n]+=1

for k in K:
    K_d.setdefault(k, 0)
    K_d[k]+=1

res = 'NO'
if K_d == N_d:
    res = 'YES'

print(res)

print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')

a = input()
print(a)
