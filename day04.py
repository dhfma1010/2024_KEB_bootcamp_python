# dictionary 안주 추천 프로그램 + random
import random


drinks_foods = {"위스키": "초콜릿", "와인":"치즈", "소주":"삼겹살", "고량주":"양꼬치"}

# drink = input(drinks_foods.keys())
drinks_foods_keys = list(drinks_foods) # dic을 list로 감싸면 key만 저장됨.
# print(drinks_foods_keys)

random_drink = random.choice(drinks_foods_keys) # random모듈의 choice함수 sequence


while True:
    menu = input(f'다음 술 중에 고르세요.\n1) {drinks_foods_keys[0]}, 2) {drinks_foods_keys[1]}, 3) {drinks_foods_keys[2]}, 4) {drinks_foods_keys[3]} 5) 아무거나  6) 종료: ')
    if menu == '1':
        print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]} 입니다.')

    elif menu == '2':
        print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]} 입니다.')

    elif menu == '3':
        print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]} 입니다.')

    elif menu == '4':
        print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]} 입니다.')

    elif menu == '5':
        random_drink = random.choice(drinks_foods_keys)  # 여기에 안하면 while 바깥에서 고정돼서 돌아감
        print(f'{random_drink}에 어울리는 안주는 {drinks_foods[random_drink]} 입니다.')


    elif menu == '6':
        print(f'다음에 또 오세요.')
        break

    print()

