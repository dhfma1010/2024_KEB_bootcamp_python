# Assignment 1 create dict

# 8.1
e2f = dict(dog='chien', cat='chat', walrus='morse')
print(e2f)

e2f_2 = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
print(e2f_2)

# 8.2 값 얻기

print(e2f['walrus'])
print(e2f.get('walrus'))

# 8.3 f2e

print(e2f.keys()) # e2f.keys()는 dict_keys class(타입)
print(e2f.values())

f2e_values = list(e2f.keys()) # 리스트로 변환
print(f2e_values)
f2e_keys = list(e2f.values())
print(f2e_keys)

f2e = dict(zip(f2e_keys,f2e_values)) # zip사용해서 dict만듦
f2e_2 = {key: value for key, value in zip(f2e_keys,f2e_values)}  # dictionary comprehention
e2f_3 = dict(zip(f2e_values,f2e_keys))
print(f2e)
print(f2e_2)
print(e2f_3)