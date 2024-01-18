# def squares(n):
#    return n * n

even_numbers = [i for i in range(51) if i % 2 == 0]
print(even_numbers)

# print(tuple(map(squares, even_numbers)))

print(tuple(map(lambda x: x**2, even_numbers))) # squares 함수 없어도 됨/ 대신 익명함수
# 아래도 같은 결과
# z = lambda x: pow(x,2)
# print(tuple(map(z,even_numbers)))