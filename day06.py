class FlyingMixin:
    def fly(self):
        return f"{self.name}이(가) 하늘을 납니다."
class SwimmingMixin:
    def swim(self):
        return f"{self.name}이(가) 수영"

class Pokemon:
    def __init__(self, name):
        self.name = name
    def attack(self):
        print("공격")

class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")

print(g1.name)
g1.name = "잉어킹" # direct로 변경
print(g1.name)


# print(c1.fly())
# print(g1.swim())
# c1.attack()
# Charizard.attack(c1) # 원래 객체명.메소드() self.attack() // class.attack(self) 클래스 이름 올 경우 객체명(g1,c1등) 괄호 안에 넣어야 함
# # Charizard.attack() # 오류남

