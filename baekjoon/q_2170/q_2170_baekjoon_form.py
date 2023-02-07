import sys


def solution():
    N = int(input())
    line = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    line = sorted(line, key=lambda x: x[0])

    l, left, right = 0, line[0][0], line[0][1]

    for i in line[1:]:
        # 안 겹치면
        if right < i[0]:
            l = l + (right - left)
            left, right = i[0], i[1]
        right = max(right, i[1])

    l = l + (right - left)
    print(l)


if __name__ == "__main__":
    solution()
