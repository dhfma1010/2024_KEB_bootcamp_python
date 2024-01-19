def desc():
    def wrapper(): # 호출하지 않으면 실행되지 않음
        print("study")
    print("a")
    return wrapper

desc() # wrapper실행 안됨


def something():  # 건드리지 않고 확장 -> 데코레이터
    print("do something")

something()
