import sys

sys.stdin = open('in5.txt', 'rt')
n = 10
cards = [str(i) for i in range(1, 21)]

indexs = []

for i in range(n):
    idx = map(int, input().split())
    idx_tu = tuple(idx)
    indexs.append(idx_tu)


def _reverser(nums, start, end) -> None:
    real_start = start - 1
    nums_target = nums[real_start:end]
    nums_re = nums_target[::-1]

    idx = 0
    for i in range(real_start, end):
        nums[i] = nums_re[idx]
        idx = idx + 1


for i in range(n):
    _reverser(cards, indexs[i][0], indexs[i][1])

for card in cards:
    print(card, end=' ')

print()
print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())


print('======== extra checker ========')
sys.stdin = open('out5.txt', 'rt')
cards_answer = list(map(int, input().split()))

for i in range(n):
    if cards_answer[i] != int(cards[i]):
        print(f"There is False answer :: {cards_answer[i]} :: {cards[i]}")
        break
