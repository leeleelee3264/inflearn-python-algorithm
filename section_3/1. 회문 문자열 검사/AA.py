import sys

sys.stdin = open('in5.txt', 'rt')
n = int(input())
letters = []
results = []

for i in range(n):
    letters.append(input())

for i in range(n):
    g = letters[i]
    g_reverse = g[::-1]

    counter = 0
    for j in range(len(g)):
        if g[j].lower() == g_reverse[j].lower():
            counter = counter + 1

    result = 'NO'
    if counter == len(g):
        result = 'YES'

    results.append(result)

for result in range(n):
    print(f'#{result + 1} {results[result]}')


print("-------")
print("-------")

sys.stdin = open('out5.txt', 'rt')

for i in range(n):
    print(input())
