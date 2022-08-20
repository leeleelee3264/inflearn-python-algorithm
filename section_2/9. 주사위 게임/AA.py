import sys

sys.stdin = open('in4.txt', 'rt')
n = int(input())


def none_same(this_max):
    price = 100 * this_max
    return price


def two_same(this_same):
    price = 1_000 + this_same * 100
    return price


def all_same(this_same):
    price = 10_000 + this_same * 1_000
    return price


prices = [0] * (n + 1)

for i in range(n):
    nums = list(map(int, input().split()))

    if nums.count(nums[0]) == 3:
        prices[i] = all_same(nums[0])
    elif nums.count(nums[0]) == 2:
        prices[i] = two_same(nums[0])
    elif nums.count(nums[0]) == 1:
        if nums.count(nums[1]) == 2:
            prices[i] = two_same(nums[1])
        else:
            this_max = max(nums)
            prices[i] = none_same(this_max)


print(max(prices))

print('-----')
print('-----')
sys.stdin = open('out4.txt', 'rt')
print(input())
