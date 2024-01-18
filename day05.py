# assignment 9.2 generator

def get_odds():
    n = [i for i in range(10) if i % 2 == 1]
    yield n


print(get_odds(), type(get_odds()))

for number in get_odds():
    print(number[2])
