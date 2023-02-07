def solution(n, line):
    line = sorted(line, key=lambda x: x[0])

    l, left, right = 0, line[0][0], line[0][1]

    for i in line[1:]:
        # 안 겹치면
        if right < i[0]:
            l = l + (right - left)
            left, right = i[0], i[1]
        right = max(right, i[1])

    l = l + (right - left)
    return l


n = 4
line = [
    [1, 3],
    [2, 5],
    [3, 5],
    [6, 7],
]

print(solution(n, line))
