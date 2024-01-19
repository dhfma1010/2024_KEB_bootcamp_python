# assignment

def test(f):
    """
    데코레이터 함수, 함수 시작 start 출력, 끝나면 end 출력
    :param f: function
    :return: closure function
    """
    # def test_in(*args, **kwargs):  #매개변수 지워도 되고 작성해도 됨
    def test_in()
        print('start')
        # result = f(*args, **kwargs)
        f()  # 호출만 해도 됨
        print('end')
        # return result
    return test_in # closure 리턴해야함!!



# 수동
def greeting():  # 기존함수 수정 안함! 닫혀있음
    print("안녕하세요")

t = test(greeting)
t()
