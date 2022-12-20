import sys

sys.stdin = open('in5.txt', 'rt')
a = input()
aa = [ch for ch in a]

stack = []

idx = 0

while idx < len(aa):
    if aa[idx].isdigit():
        stack.append(aa[idx])
        idx+=1
    else:
        op = aa[idx]
        a2 = int(stack.pop())
        a1 = int(stack.pop())
        a3 = 0

        if op=='*':
            a3 = a1*a2
        elif op =='/':
            a3 = a1/a2
        elif op=='+':
            a3 = a1+a2
        elif op=='-':
            a3 = a1-a2

        stack.append(a3)
        idx+=1

print(stack[0])

sys.stdin = open('out5.txt', 'rt')
a = input()
print('-----')
print('-----')
print(a)
