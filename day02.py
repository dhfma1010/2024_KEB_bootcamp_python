base_number = int(input('Input base number : '))
exponent_number = int(input('Input exponent number : '))
# print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {base_number**exponent_number}')
# 1) f-string , {}: 값 바뀔 변수, 함수 리턴 값
print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {pow(base_number,exponent_number)}')

# 2) format function , 3.6v 하고도 호환됨
print('밑은 {0}, 지수는 {1}, 결과 값은 {2}'.format(base_number,exponent_number,pow(base_number,exponent_number)))
print('밑은 {}, 지수는 {}, 결과 값은 {}'.format(base_number,exponent_number,pow(base_number,exponent_number)))

# 3) c like
print('밑은 %d, 지수는 %d, 결과 값은 %d' % (base_number, exponent_number, pow(base_number,exponent_number)))


# money = 5,000,000
# print(money)
# print(type(money)) # tuple
# cash = 5_000_000
# print(cash)
# print(type(cash)) # int




