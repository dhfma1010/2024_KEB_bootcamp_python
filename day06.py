def factorial_repetition(n)-> int: # 장점 : 속도 빠름
    """
    반복문을 이용한 팩토리얼 함수
    :param n: 정수, int
    :return: 팩토리얼 값, int
    """
    result = 1  # 값 바뀔 문제
    for i in range(2, n+1): # 값 바뀔 문제
        result = result * i
    return result

def factorial_recursion(n): # 실수할 여지 적음. 메모리 많이 사용. (스택)
    """
    재귀함수를 사용한 팩토리얼 함수
    :param n: 정수, int
    :return: function
    """
    if n == 1:
        return n
    else:
        return n * factorial_recursion(n-1)

number = int(input("number : "))
print(factorial_recursion(number))

print(factorial_repetition(number))