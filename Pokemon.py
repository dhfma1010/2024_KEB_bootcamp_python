
class Pokemon:
    def __init__(self, num, name, hp, type, ability, weakness):
        self.num = num+1
        self.name = name
        self.hp = hp
        self.type = type
        self.ability = ability
        self.weakness = weakness

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")
        if self.hp > target.hp:
            target.hp = target.hp - self.hp
            print(f'{target.name}의 hp가 {target.hp}로 감소했습니다.')
        else:
            print(f'{self.name}의 공격이 {target.name}에 영향을 미치지 못했습니다.')


class Oddish:
    def attack(self):
        print("잎날 가르기 공격!")

    def evolution(self, evolution1):
        print(f'{p1.name}이 {evolution1}으로 진화')
        p1.name = evolution1


class Charmander:
    def attack(self):
        print("불토하기 공격!")

    def evolution(self, evolution1):
        print(f'{p2.name}이 {evolution1}으로 진화')
        p2.name = evolution1

class Finizen:
    def attack(self):
        print("지느러미 커터 공격!")

    def evolution(self, evolution1):
        print(f'{p3.name}이 {evolution1}으로 진화')
        p3.name = evolution1

# 포켓몬 생성
p1 = Pokemon(1, "뚜벅쵸", 60, "Grass", "Chlorophyll", "Fire") # 뚜벅쵸
p2 = Pokemon(2, "파이리", 70, "Fire", "Blaze", "Water")  # 파이리
p3 = Pokemon(3, "맨돌핀", 50, "Water", "Water Veil", "Grass")  # 맨돌핀

choice_pokemon = int(input("Choice Pokemon : 1) Oddish 2) Charmander 3) Finizen : " ))

if choice_pokemon == 1:

    print(f'You choose {p1.name}')

    while True:
        attack_to = input("공격 대상 선택 Charmander or Finizen? : ")
        print(p1.attack)

        if p2.hp < 0 or p3.hp < 0:
            print("공격 대상이 기절하였습니다.")
            break

        else:
            if attack_to == "Charmander":
                p1.attack(p2)
            elif attack_to == "Finizen":
                p1.attack(p3)
            else:
                print("공격 대상의 이름을 정확히 입력하시오. ")






elif choice_pokemon == 2:
    print(f'You choose {p2.name}')

elif choice_pokemon == 3:
    print(f'You choose {p3.name}')








#
#
#
# class FlyingBehavior:
#     def fly(self):
#         return f"하늘을 훨훨 날아갑니다~"
#
# class NoFly(FlyingBehavior):
#     def fly(self):
#         return f"하늘 날 수x"
#
# class FlyWithWings(FlyingBehavior):
#
#     def fly(self):
#         return f"날개로 하늘 날아"
#
#
# class JetPack(FlyingBehavior):
#     def fly(self):
#         return f"로켓으로 하늘 날아감"
#
#
# class SwimmingBehavior:
#     def swim(self):
#         return f"{self.__name}이(가) 수영을 합니다."
#
#
# nofly = NoFly()
# p1 = Pikachu("피카츄", 35, nofly)
# print(p1.fly_beh.fly()) # aggregation