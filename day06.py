# class Pokemon():
class Pokemon:
    def __init__(self, name): # 생성자, 각 개체마다 딱 1번 돌아가는 코드
        print(f"{name} 포켓몬스터 생성")


pikachu = Pokemon("피카츄")
squirtle = Pokemon("꼬부기")

print(pikachu)  # <__main__.Pokemon object at 0x000002222DBFD340> main안에 Pokemon 객체
                ## -> 원하는 방식으로 출력되게 가능
print(squirtle)

