# 매개변수로 함수 들어갈 수 있음

def squares(n):
    return n * n

def run_function(f, number):
    return f(number)

print(squares(7))
print(run_function(squares,9))