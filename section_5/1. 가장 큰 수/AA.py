import sys

sys.stdin = open('in4.txt', 'rt')

m = int(input())
nums = list(map(int, input()))

r_l = len(nums) - m
r = [0] * r_l

idx = 0
d_c = 0

while nums and r_l > 0:
    l = len(nums)

    for i in range(len(nums)):
        if r[idx] < nums[i] and (l-i) > r_l -1:
            r[idx] = nums[i]
            d_c = i

    for j in range(d_c+1):
        nums.pop(0)
    idx+=1
    r_l-=1



print(''.join(map(str,r)))
print('-----')
print('-----')
sys.stdin = open('out4.txt', 'rt')
res = input()
print(res)
print('-----')
print('-----')
print(''.join(map(str,r)) == res)
