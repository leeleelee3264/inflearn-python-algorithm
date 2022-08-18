# 반복문을 이용한 문제 풀이

n = input('please insert number ')
n = int(n)

# 1
for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    print(i)

print("--")
print("--")

# 2
total_sum = 0
for i in range(1, n + 1):
    total_sum = total_sum + i

print(total_sum)

print("--")
print("--")

# 3
for i in range(1, n):
    if n % i == 0:
        print(i)
