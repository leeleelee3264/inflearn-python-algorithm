import sys

# bin() 이 아니고서 2진수로 변환하는 방법을 모르겠다!!
sys.stdin = open('in4.txt', 'rt')
N = int(input())

def decimal_to_binary(decimal_num):
    if decimal_num <= 1:
        return str(decimal_num)
    else:
        return decimal_to_binary(decimal_num // 2) + str(decimal_num % 2)




print(decimal_to_binary(N))

print('-----')
print('-----')
sys.stdin = open('out4.txt', 'rt')

a = input()
print(a)