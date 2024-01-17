t1 = (5)
t2 = 5,
t3 = (5,)
t4 = (5, 7)
t5 = 5, 7

print(type(t1),type(t2),type(t3),type(t4),type(t5))

t6 = "python", "kim" # packing

print(type(t6), t6[1])
subject, prof = t6 # unpacking 개수 맞아야
# a, b, c = t6   # ValueError: not enough values to unpack
print(prof)
print(subject)

t7 = () # 빈 튜플
t8 = tuple()   # 자료구조 튜플로 형 변환
print(type(t7), type(t8), type(9,), type((9,)))  # 3번째것은 쉼표 구분기호 -int/ 4번째 것은 괄호때문에 튜플로

print(type('Groucho',))  # 문자열로


# 튜플간 비교연산 가능
t9 = 1, 2, 3
t10 = 1, 2
print(t9 == t10)
print(t9 <= t10)
print(t9 > t10)

t11 = 4.43,
t12 = 3.88, 4.1, 3.26

# print(t11 + t12)
print(id(t11))
t11 = t11 + t12 # t11 += t12
print(id(t11))
print(t11)