import sys

sys.stdin = open('in5.txt', 'rt')
n = map(int, input().split())
student = list(map(int, input().split()))

avg = round(sum(student) / len(student))

target_student = 0
smallest = 100

for i in range(len(student)):
    closer = abs(avg - student[i])
    if closer < smallest:
        smallest = closer
        target_student = i

print(f'{avg} {target_student+1}')

print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
