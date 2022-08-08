# chapter 2 변수입력과 연산자
a = input('슷자를 입력하세요: ')
print(a)

a, b = input('슷자를 입력하세요: ').split()
print(a + b)
print(int(a) + int(b))

a, b = map(int, input('슷자를 입력하세요: ').split())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

a = 4.3
b = 5
c = a + b
# 실수가 정수보다 범위가 더 크기 때문에 더 큰 형인 float으로 연산이 된다.
print(type(c))
