import sys

sys.stdin = open('in5.txt', 'rt')

n = 9
a = []

for i in range(n):
    _ = list(map(int, input().split()))
    a.append(_)

def check_rows(a) -> bool:
    for x in a:
        s = set(x)
        if len(s) != n:
            return False
    return True

def check_cols(a) -> bool:
    dx= [0, 1, 2, 3, 4, 5, 6, 7, 8]

    for y in range(n):
        s = set(a[dx[k]][y] for k in range(n))
        if len(s) != n:
            return False
    return True

def check_subs(a) -> bool:
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, -1, 1, -1, 1]

    for x in range(1, 9, 3):
        for y in range(1, 9, 3):
            s = set(a[x+dx[k]][y+dy[k]] for k in range(8))
            s.add(a[x][y])

            if len(s) != n:
                return False
    return True


result = 'NO'

if check_rows(a):
    if check_cols(a):
        if check_subs(a):
            result = 'YES'

print(result)
print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
#
# a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
#
# dx = [-1, 0, 1, 0, -1, -1, 1, 1]
# dy = [0, 1, 0, -1, -1, 1, -1, 1]
#
# x = 1
# y = 1
#
# print(a[x][y])
#
# for k in range(7):
#     _x = x + dx[k]
#     _y = y + dy[k]
#     re = a[_x][_y]
#     print(re)
#
