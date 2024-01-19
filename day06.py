import random

class OoopsException(Exception): # 괄호 안 상속
    pass

numbers = []
for i in range(5):
    numbers.append(random.randint(1, 100))
print(numbers)


# 줄이기

numbers = [random.randint(1,100) for i in range(10)]
print(numbers)

try:
    pick = int(input(f'Input index (0 ~ {len(numbers)-1}) : '))
    print(numbers[pick])
    print(5/2)
    raise OoopsException("Oops")  # exception!


# except: # 모든 걸 잡음. 에러 아닌 것도!

except IndexError as err:  # as err: 시스템이 던져준 에러 # numbers[pick]에서 에러 발생
    print(f"Wrong index number \n{err}")
except ValueError as err:  # input은 받는데 int로 넘어갈 때 에러
    print(f"Input Only Number \n{err}")
except ZeroDivisionError as err:
    print(f"The denominator cannot be 0. \n{err}")

#except OoopsException as err:
#    print(f'Oops Oops {err}')

except Exception as err : # 가장 마지막에 와야함! !
    print(f"Error occurs : {err}")

else:
    print(f'Program terminate')