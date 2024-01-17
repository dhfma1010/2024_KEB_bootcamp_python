# Assignment 1 create dict

# 8.1
e2f = dict(dog='chien', cat='chat', walrus='morse')
print(e2f)

# 8.5

e2f_keys_tuple = tuple(e2f.keys())
e2f_keys_list = list(e2f.keys())
print(f'English words : {e2f_keys_tuple}')
print(f'English words : {e2f_keys_list}')

print('English words :', end=' ')
for eng_word in e2f_keys_tuple:
    print(eng_word, end=' ')