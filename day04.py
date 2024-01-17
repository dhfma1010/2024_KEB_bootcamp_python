# list 컴프리헨션

# 1)
# squares = list()
# squares.append(1*1)
# squares.append(2*2)
# squares.append(3*3)
# squares.append(4*4)
# squares.append(5*5)
# print(squares)

# 2)
# squares = list()
# for i in range(1,6):
#     squares.append(i*i)
# print(squares)

# 3) list comprehension 축약표현  -------- for문 여러개 일때는 가독성 문제로 잘 안씀
# squares = [i*i for i in range(1,6,1)]
# print(squares)

even_squares = [i*i for i in range(1, 6, 1) if i % 2 == 0]
print(even_squares)  # 리스트 초기화 할 때 유용
