# 6-3

guess_me = 5

for number in range(10):
    if guess_me > number:
        print("too low")
    elif guess_me == number:
        print("found it!")
    elif guess_me < number:
        print("oops")
        break

## number 0부터 시작해도 되나??