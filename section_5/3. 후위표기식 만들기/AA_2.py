import sys

sys.stdin = open('in5.txt', 'rt')
a = input()
aa = [ch for ch in a]

c = []
res = ''


for a in aa:
    if a.isdigit():
        res+=a
    else:
        if a == '(':
            c.append(a)
        elif a in ('*', '/'):
            while c and c[-1] in ('*', '/'):
                res+=c.pop()
            c.append(a)
        elif a in ('+', '-'):
            while c and c[-1] != '(':
                res+=c.pop()
            c.append(a)
        elif a == ')':
            while c and c[-1] != '(':
                res += c.pop()
            c.pop()


while c:
    res+=c.pop()

print(res)
print('-----')
sys.stdin = open('out5.txt', 'rt')
a = input()
print(a)
print('-----')
print(res == a)