x = 2
y = x + 5 # NameError: name 'x' is not defined
print(y)

print(type(3.14))
print(type(3.14) == float)
print(isinstance(3.14, float))
print(isinstance("inta", float))
print(isinstance(55, float))

artist = ['BTS', '뉴진스', '핑클', 'SES', 'HOT', '블랙핑크']
groups = artist # 복제가 아니라 참조 개념!!!!!
print(artist, groups)
artist[2] = '세븐틴'
print(artist, groups)



