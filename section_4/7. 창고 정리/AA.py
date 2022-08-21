import sys


sys.stdin = open('in5.txt', 'rt')
n = int(input())

boxes = list(map(int, input().split()))

m = int(input())

for i in range(m):
    this_max = max(boxes)
    this_min = min(boxes)

    max_idx = boxes.index(this_max)
    min_idx = boxes.index(this_min)

    boxes[max_idx] = this_max - 1
    boxes[min_idx] = this_min + 1


final_max = max(boxes)
final_min = min(boxes)

print(final_max - final_min)

print('-----')
print('-----')
sys.stdin = open('out5.txt', 'rt')
print(input())
