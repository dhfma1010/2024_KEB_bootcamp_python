# prime number with fuction
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

while True:

    menu = input("1) Fahrenheit -> Celsius 2) Celsius -> Fahrenheit 3) prime number or not 4) n1~n2 prime numbers 5) Quit program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0/9.0):.4f}C')

    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius * 9.0/5.0) + 32.0):.4f}F')

    elif menu == '3':
        number = int(input("Input number : "))

        if isprime(number):  # remove ==
            print(f'{number} is prime number')
        else:
            print(f'{number} is NOT prime number!')

    elif menu == '4': # 엄청 큰 소수 입력했을 때 반복문 계속 돌아가는 문제
        n1, n2 = map(int, input("Input first second number : ").split())
        n1, n2 = min(n1, n2), max(n1, n2)

        # numbers = input("Input first second number : ").split()  # 숫자 입력하는 방식 설명해주는 것 개선! n1(space)n2 )    # 가독성 있게 코드 개선 5줄 -> 2줄?
        # n1 = int(numbers[0])
        # n2 = int(numbers[1])

        # if n1 > n2:
        #   n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            if isprime(number):
                print(number, end=' ')
        print()

    elif menu == '5':
        print('Terminate Program.')
        break

    else:

        print("Invalid Menu")