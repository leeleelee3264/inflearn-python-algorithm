import sys

sys.stdin = open('in5.txt', 'rt')
n = int(input())


# nums = [0 for i in range(n + 1)]
# 더 간단한 방식
nums = [0] * (n + 1)
cnt = 0

for i in range(2, n + 1):
    if nums[i] == 0:
        cnt = cnt + 1
        # for j in range(i + 1, n + 1):
        # 나 자신부터 -1로 만들어준다.
        # 1 씩 증가하는 게 아니라 i 씩 증가하게 해서 효율을 높힌다.
        for j in range(i, n + 1, i):
           # i 씩 증가하면 무조건 배수니까 if 조건을 걸어서 확인을 할 필요가 없다.
           # if j % i == 0:
            nums[j] = -1

print(cnt)

print('-----')
print('-----')
with open('out5.txt', 'rb') as f:
    contents = f.read()
    contents_str = contents.decode('utf-16')
    print(contents_str)
