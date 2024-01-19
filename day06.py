# class Pokemon():

# 객체에 속성 할당

class Pokemon:
    pass

pikachu = Pokemon()
squirtle = Pokemon()
pikachu.name = "피카츄"
pikachu.nemesis = squirtle
print(pikachu.name)
# print(pikachu.nemesis.name) # 오류!

# squirtle.name = "꼬부기"
pikachu.nemesis.name = "꼬부기"
print(pikachu.nemesis.name)  # 할당 후 오류 안남!
print(squirtle.name)
