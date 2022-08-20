import sys

sys.stdin = open('in5.txt', 'rt')
n = int(input())
nums = list(map(int, input().split()))


def reverse(x):
    str_x = str(x)
    str_reverse = str_x[::-1]

    return int(str_reverse)


def is_prime(x):
    if x == 1:
        return False

    nums = [0] * (x + 1)

    for i in range(2, x + 1):
        if nums[i] == 0:
            for j in range(i, x + 1, i):
                if i == j:
                    continue
                nums[j] = -1

    if nums[x] == 0:
        return True

    return False


for num in nums:
    num_reverse = reverse(num)
    if is_prime(num_reverse):
        print(num_reverse, end=' ')


print()
print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())

