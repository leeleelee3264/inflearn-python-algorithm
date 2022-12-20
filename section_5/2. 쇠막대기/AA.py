import sys

sys.stdin = open('in5.txt', 'rt')
a = input()

# 헷갈리니까 레이저 바꾸는 작업 해주기
_aa = a.replace('()', '0')
aa = [ch for ch in _aa]

n_stack = []
res = 0

for i in range(len(aa)):
    if aa[i] == '(':
        n_stack.append(i)
    elif aa[i] == ')':
        s = n_stack.pop()
        e = i

        _aa = aa[s:e+1]
        laz = 0
        for a in _aa:
            if a == '0':
                laz+=1
        res+= (laz+1)



print(res)
print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
a = input()
print(a)
