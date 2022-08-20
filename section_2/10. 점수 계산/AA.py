import sys

sys.stdin = open('in5.txt', 'rt')
n = int(input())
a = list(map(int, input().split()))

score = 0
correct = False
correct_count = 0

for i in a:
    if i == 1:
        if not correct:
            correct = True
            correct_count = 1
        else:
            correct_count = correct_count + 1
    else:
        correct = False
        correct_count = 0
    score = score + correct_count

print(score)

print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
