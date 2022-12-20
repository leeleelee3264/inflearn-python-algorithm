import sys

def is_lower_than_me(src, dest):
    one = ['+', '-']
    two = ['*', '/']

    if dest == '(':
       return True

    if dest in one and src in two:
        return True
    elif dest in two:
        return True

    return False

sys.stdin = open('in2.txt', 'rt')

a = input()
aa = [ch for ch in a]

c = []
res = ''

for i in aa:
    # 피연산자는 그대로 출력
    if i.isdigit():
        res+=i
    else:
        if not c:
            c.append(i)
        elif i == '(':
            c.append(i)
        elif i == ')':
            while True:
                top = len(c) - 1
                if c[top] == '(':
                    c.pop()
                    break
                res += c[top]
                c.pop()
        else:
            while c:
                top = len(c) -1
                # 안에 있는 게 우선 순위가 높 때 나를 넣는다.
                if is_lower_than_me(i, c[top]):
                    c.append(i)
                    break
                else:
                    # 안에 있는 게 우선순위가 같거나 높을 때 계속 꺼낸다.
                    res+=c[top]
                    c.pop()

while c:
    top = len(c) - 1
    res+=c[top]
    c.pop()

print(res)
print('-----')
sys.stdin = open('out2.txt', 'rt')
a = input()
print(a)
print('-----')
print(res == a)