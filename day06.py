# assignment

def get_odds(n) -> int:
    """
    1부터 n까지 홀수를 발생시키는 제너레이터
    :param n: int
    :return: int
    """
    for i in range(1,n+1,2):
        yield i # i값 계속 보내줌 , 이전 상태 사라짐

cnt = 0
odds = get_odds(9)

for odd in odds:
    cnt = cnt + 1
    if cnt == 3:
        print(f'Third number is {odd}')
        break


# 제너레이트 이므로 또 반복 안되고 사라짐
for odd in odds:
    cnt = cnt + 1
    if cnt == 3:
        print(f'Third number is {odd}')
        break