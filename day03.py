university = "Inha\nUniversity!"
# university = r"Inha\nUniversity" # raw string

# slicing
# print(university[:4])
# print(university[:-11]) # reverse
# print(len(university))   # len 문자열 길이
# print(university[0:len(university)])
# print(university[0:16])
# print(university[:16])
# print(university[::2])




nuber1 = input("First number :")
nuber2 = input("Second number :")
print(nuber1 + nuber2) # concatenation
print(nuber1 * 3) # duplication
# print(nuber1 + 3) # TypeError: can only concatenate str (not "int") to str


name = 'aabbccdd'
name.replace('cc','ee')
print(name)

course = "2024 KEB bootcamp"
print(course)
list_course = course.split()
print(list_course)