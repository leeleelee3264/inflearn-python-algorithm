import sys


sys.stdin = open('in4.txt', 'rt')

m = int(input())
nums = list(map(int, input()))

# 풀이는 맞았는데 기본 컨셉이 틀렸다.
# 결국 중요한 것은, 내가 들어갈 때 내 앞에 있는 것이 작으면, 그걸 지우고 들어가야 한다는 것이다. (이때 스텍에 넣고, 제일 최근 값인 나의 앞에 값을 빼주는 것임)

# 내가 스텍에 들어간다. 내 앞에 애가 나보다 작으면 지우고, delete 카운트를 하나 내린다.

r_l = len(nums) - m
r = [nums[0]]

for i in range(1, len(nums)):
    if len(r) == r_l:
        break

    if r[len(r)-1] >= nums[i]:
        r.append(nums[i])
    elif m == 0:
        r.append(nums[i])
    else:
        while True:
            r.pop()
            m -=1
            if not r or m == 0 or r[len(r)-1] >= nums[i]:
                r.append(nums[i])
                break


print(''.join(map(str,r)))
print('-----')
print('-----')
sys.stdin = open('out4.txt', 'rt')
res = input()
print(res)
print('-----')
print('-----')
print(''.join(map(str,r)) == res)
