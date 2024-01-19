# # class Pokemon():
#
# # 객체에 속성 할당
#
# class Pokemon:
#     pass
#
# pikachu = Pokemon()
# squirtle = Pokemon()
# pikachu.name = "피카츄"
# pikachu.nemesis = squirtle
# print(pikachu.name)
# # print(pikachu.nemesis.name) # 오류!
#
# # squirtle.name = "꼬부기"
# pikachu.nemesis.name = "꼬부기"
# print(pikachu.nemesis.name)  # 할당 후 오류 안남!
# print(squirtle.name)




class Pokemon:
    def __init__(self, name):  # 여기 name은 클래스의 속성 아님! 그냥 단순 출력
        self.name = name # 이 코드가 클래스 속성 넣는 것
        print(f"{name} 포켓몬스터 생성")

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")

charizard = Pokemon("리자몽")
pikachu = Pokemon("피카츄")
squirtle = Pokemon("꼬부기")
charizard.attack(squirtle)
print(pikachu.name)
print(squirtle.name)
