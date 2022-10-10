n = int(input())

b = 0

while n > -1:
    if n % 5 == 0:
        b = b + (n // 5)
        break
    n = n - 3
    b = b + 1
else:
    b = -1

print(b)
