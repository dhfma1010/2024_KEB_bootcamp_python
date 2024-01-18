# prime number  # 두 수 사이의 소수 출력 + 함수사용
def isprime(n) -> bool: # type hint(생략해도 됨!)
    """
    매개변수로 넘겨 받은 수가 소수인 여부를 boolean으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True, 소수가 아니면 False
    """
    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True



numbers = input("Input first second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

# is_prime = True ## 여기 있으면 소수 전체 출력 안됨!!
for number in range(n1, n2+1):
        if isprime(number):
            print(number, end=' ')