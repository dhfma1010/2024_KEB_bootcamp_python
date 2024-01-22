# 매직 메서드

class FlyingMixin:
    def fly(self):
        return f"{self.__name}이(가) 하늘을 훨훨 날아갑니다~"

class SwimmingMixin:
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name):
        self.__name = name

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

    def __add__(self, other):
        list1=self.name[0:2]
        list2=other.name[-1]
        name=list1+list2
        return str(name)


class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
print(g1)  # <__main__.Gyarados object at 0x000001A6A078E0C0>
print(c1)

print(g1+c1) # 정수나 문자 연산 + 아니므로 오류 / 새로 매직메서드 필요