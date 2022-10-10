import sys

sys.stdin = open('in5.txt', 'rt')
n = input()


def _count_divisor(num):
    counter = 0

    for i in range(1, num + 1):
        if num % i == 0:
            counter = counter + 1

    return counter


nums = ''
n_str = list(n)

for i in range(len(n_str)):

    try:
        tmp = int(n_str[i])
        nums = nums + n_str[i]
    except ValueError:
        pass

nums_int = int(nums)

print(int(nums))
print(_count_divisor(nums_int))

print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
print(input())
