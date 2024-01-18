# assignment 예외정의

class OopsException(Exception):
    pass

words = []
while True:
    word = input("Input word: ")
    words.append(word)

    if 'oops' in words:
        raise OopsException(word)

    print(words)

try:
    raise OopsException('Caught an oops')
except OopsException as exc:
    print(exc)



