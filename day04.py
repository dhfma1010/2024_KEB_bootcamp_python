# Assignment 1 create dict

# 8.1
e2f = dict(dog='chien', cat='chat', walrus='morse')
print(e2f)

# 8.4

e2f_keys = list(e2f.keys())
e2f_values = list(e2f.values())

reverse_e2f = {value: key for value,key in zip(e2f_values,e2f_keys)}
print(reverse_e2f.get('chien'))

# 추가로

French_word = input('프랑스 단어 입력 chien / chat / morse : ')
print(reverse_e2f.get(French_word))

# 번역 프로그램 만들어 볼 수 있음