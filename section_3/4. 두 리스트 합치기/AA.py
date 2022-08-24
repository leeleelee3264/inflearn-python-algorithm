import sys

sys.stdin = open('in5.txt', 'rt')
n = int(input())
n_nums = list(map(int, input().split()))
m = int(input())
m_nums = list(map(int, input().split()))


merged_nums = n_nums + m_nums
merged_nums.sort()

for nums in merged_nums:
    print(nums, end=' ')


print()
print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())

print('======== extra checker ========')
sys.stdin = open('out5.txt', 'rt')
cards_answer = list(map(int, input().split()))

for i in range(n):
    if cards_answer[i] != merged_nums[i]:
        print(f"There is False answer :: {cards_answer[i]} :: {merged_nums[i]}")
        break
