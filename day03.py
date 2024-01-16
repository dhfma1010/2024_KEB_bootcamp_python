
course = "* KEB 2024#! KEB !bootcamp KEB...*!#"
print(course.find('KEB'))  # 앞에서 부터 찾기
print(course.rfind('KEB'))   # 뒤에서 부터 찾기
print(course.index('KEB'))  # find랑 같은 기능
print(course.rindex('KEB'))  # find랑 같은 기능
print(course.find('Inha'))  # -1  --> if문 사용해서 해결
print(course.index('Inha')) # ValueError: substring not found


print(course)
course = course.replace('KEB','Inha',2)
print(course)

print(course.strip())
print(course.strip("!#.*"))  # 연속적인 것,맨 앞쪽 지워짐, 중간중간 안지워짐




# print(course)
# print(course.replace('KEB','Inha'))
# print(course)
# course = course.replace('KEB','Inha')
# print(course) # 재할당 됨

