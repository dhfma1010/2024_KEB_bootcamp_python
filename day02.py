letter = input('Input alphabet letter : ')
# vowels = {'a', 'e', 'i', 'o', 'u'}
# print(type(vowels)) , set 클래스
vowels = "aeiou" # str
if letter in vowels:
    print(f'{letter} is a vowel')
else:
    print(f'{letter} is a consonant')