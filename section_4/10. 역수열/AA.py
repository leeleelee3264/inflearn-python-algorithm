import sys

sys.stdin = open('in5.txt', 'rt')
n = int(input())
nums = list(map(int, input().split()))

result = [0] * n

# 빈 공간만 찾으면 되는 거였다.
# 자기가 들어올 nth 번쨰 자리가 빈공간인게 아니라,
# 값들이 들어간 것을 반영하여, 앞에 빈공간이 n 개 있는 곳에 넣어야 했던 것이다.

# 빈공간 일 때 넣고, 빈공간이 아니면 하나 뒤로 밀고, 앞에 있는 작은수 구하기 -> 아니었던 것이다.
# 처음부터 앞에 빈공간이 n개 있는 것을 구하고, 그 자리에 들어갈 때 빈공간이 아니면 더 밀어줘야 한다.

for i in range(n):
    t = i + 1
    p = nums[i]
    c = 0
    idx = 0

    for j in range(n):
        if result[j] == 0:
            c+=1

        if c == p:
            idx = j+1
            break

    t_idx = idx
    for idx2 in range(idx, n):
        if result[idx2] !=0:
                idx+=1
        else:
            break
    result[idx] = t




print(' '.join(map(str,result)))
print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
a = input()
print(a)

print('-----')
print('-----')
print(a == ' '.join(map(str,result)))
