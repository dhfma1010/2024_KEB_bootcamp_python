class Pokemon:
    def __init__(self, name):
        self.name = name

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")

class Pikachu(Pokemon):  # 상속하는 법 is-a 관계
# class Pikachu: # 에러
    def __init__(self, name, type):
        super().__init__(name)  # 부모 메소드 호출
        self.type = type

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) {self.type} 공격!")

    def electric_info(self):
        print("전기 계열 공격")

class Squirtle(Pokemon):
    pass

class Agumon:
    pass

p1 = Pikachu("피카츄","불꽃")  # 부모의 name 사용
p2 = Squirtle("꼬부기")
p3 = Pokemon("아무")
print(p1.name)

print(issubclass(Pikachu, Pokemon))
print(issubclass(Agumon, Pokemon))

p1.attack(p2)
p2.attack(p1)
p1.electric_info()
# p3.electric_info() # 에러/ 자식 전용 메소드

print(p1.name, p1.type)