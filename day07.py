


class FlyingBehavior:
    def fly(self):
        return f"하늘을 훨훨 날아갑니다~"

class NoFly(FlyingBehavior):
    def fly(self):
        return f"하늘 날 수x"

class FlyWithWings(FlyingBehavior):

    def fly(self):
        return f"날개로 하늘 날아"


class JetPack(FlyingBehavior):
    def fly(self):
        return f"로켓으로 하늘 날아감"


class SwimmingBehavior:
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name, hp, fly):
        self.__name = name
        self.hp = hp
        self.fly_beh = fly  ## aggregation (has-a)

    def attack(self):
        print("공격~")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    #name = property(get_name, set_name)

    def __str__(self):  # 매직 메서드
        return self.__name + "입니다."

    # def __add__(self, other):
    #     list1=self.name[0:2]
    #     list2=other.name[-1]
    #     name=list1+list2
    #     return str(name)

    def __add__(self, target):
        # return self.name + "와 " + target.__name + "입니다."
        return f"두 포켓몬 체력 합은 {self.hp + target.hp}"    ##### 체력 늘어나고 줄어들게


class Charizard(Pokemon):
    pass

class Gyarados(Pokemon):
    pass

class Pikachu(Pokemon):
    pass



nofly = NoFly()
g1 = Pikachu("피카츄", 35, nofly)

wings = FlyWithWings() # 다른 클래스 객체 만들어서 리자몽에게 전달
c1 = Charizard("리자몽", 120, wings) # aggregation

print(c1.fly_beh.fly()) # fly객체의 fly사용
print(g1.fly_beh.fly())

print(g1)  # <__main__.Gyarados object at 0x000001A6A078E0C0>
print(c1)

print(g1+c1) # 정수나 문자 연산 + 아니므로 오류 / 새로 매직메서드 필요

