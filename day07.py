


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
class Pikachu:
    def __init__(self, name, hp, fly):
        self.name = name
        self.hp = hp
        self.fly_beh = fly


nofly = NoFly()
p1 = Pikachu("피카츄", 35, nofly)
print(p1.fly_beh.fly()) # aggregation
