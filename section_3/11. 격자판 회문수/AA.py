import sys

sys.stdin = open('in5.txt', 'rt')

n = 7
a = []
result = 0

for i in range(n):
    _ = list(map(int, input().split()))
    a.append(_)


def check_rows(a) -> int:

    ds = [0, 1, 2]
    de = [5, 6, 7]

    c = 0
    t = []

    for x in a:
        for k in range(3):
            t.append(list(x[ds[k]:de[k]]))

    for tt in t:
        r_tt = list(reversed(tt))
        if r_tt == tt:
            c+=1
    return c

def make_2d_for_cols(a):

    dx = [0, 1, 2, 3, 4, 5, 6, 7]

    tt = []
    for y in range(n):
        s = list(a[dx[k]][y] for k in range(n))
        tt.append(s)

    return tt


aa = make_2d_for_cols(a)
result = check_rows(a) + check_rows(aa)


print(result)
print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())