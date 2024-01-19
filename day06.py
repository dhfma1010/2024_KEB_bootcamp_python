def desc(f):
    def wrapper(): # 호출하지 않으면 실행되지 않음
        print("study")
        f() # 외부에서 선언된 매개변수와 같은 매개변수
    return wrapper


def something():  # 건드리지 않고 확장 -> 데코레이터
    print("do something")

something()

s = desc(something)  # wrapper(closure)가 f(외부 함수의 매개 변수) 기억하고 있음!
s()


@desc
def something():
    print("do something")

