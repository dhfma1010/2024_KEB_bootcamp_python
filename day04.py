# 튜플

t9 = 1,2,3
t10 = 3, 2

print(t9 < t10) # 개수 비교가 아니라 원소 비교!!

# 리스트

subjects = ["C++", "Java", "Python", "Java"]
print(subjects[::-1])
subjects[::-1]
print(id(subjects))
print(subjects)
subjects.reverse()  # 원본 바뀜!!!!!
print(subjects)
print(id(subjects))


print(subjects)
# #subjects.remove('Java')
# print(subjects)
# del subjects[-2]
# del subjects[1]
# print(subjects)

subjects.pop(0)
print(subjects)

