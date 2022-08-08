a, b, c = 3, 2, 1
print(a, b, c)

# 값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# 실수
a = 12.1234567891234567891234
# 12.1234567891234567 까지 나온다. float의 8 byte가 넘어가면 데이터가 손실된다.
print(a)


# 프린트 형식
a, b, c = 3, 2, 1
print(a, b, c, sep=', ')
print(a, b, c, sep=',')
print(a, b, c, sep='\n')

print(a, b, c, end=',')
