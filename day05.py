# assignment 9.3 decorator

def test(func):
    def f2(*args, **kwargs):
        print('end')
        return f1
            def f1(*args, **kwargs):
                print('start')
                result = func(*args, **kwargs)
                return result
    return f2
def subtract_ints(a,b):
    return a-b
print(subtract_ints(3,4))

@test
def subtract_ints(a,b):
    return a-b

print(subtract_ints(4,3))



