import sys


sys.stdin = open('in4.txt', 'rt')
n = int(input())

times = []


class Time:
    def __init__(self, start, end):
        self.start = start
        self.end = end


for i in range(n):
    ts = list(map(int, input().split()))
    times.append(Time(ts[0], ts[1]))

# 제일 빨리 끝나는 순으로 정렬
sorted_times = sorted(times, key=lambda x: x.end)

counter = 1
prev_idx = 0

for i in range(1, n):
    if sorted_times[i].start >= sorted_times[prev_idx].end:
        counter = counter + 1
        prev_idx = i


print(counter)

print('-----')
print('-----')
sys.stdin = open('out4.txt', 'rt')
print(input())
