import sys

sys.stdin = open('in5.txt', 'rt')
n = map(int, input().split())
student = list(map(int, input().split()))

avg = round(sum(student) / len(student))

target_student = 0
target_score = 0
smallest = 100

for i in range(len(student)):
    closer = abs(avg - student[i])
    if closer < smallest:
        smallest = closer
        target_score = student[i]
        target_student = i
    # 평균과의 거리가 같은 점수에 대한 고려를 안 해놨었다...
    # 74가 평균이면 73, 75가 대상자가 되는데 75가 값이 크니까 75가 선택이 되어야 한다.
    elif closer == smallest:
        # 여기는 동점 학생들에 대해서는 업데이트를 안 한다.
        if target_score < student[i]:
            target_score = student[i]
            target_student = i

print(f'{avg} {target_student+1}')

print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
