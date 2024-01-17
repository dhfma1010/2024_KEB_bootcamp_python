# Assignment 답안!!  (add prime series program)

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
        is_prime = True  # int -> bool

        if number < 2:
            print(f'{number} is NOT prime number!')
        else: # 중복코드 -> 함수로 만들어서 호출
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False  # remove +
                    break  # break 없으면 계속 돌아감

            # if cnt ==0:
            if is_prime:  # remove ==
                print(f'{number} is prime number')
            else:
                print(f'{number} is NOT prime number!')

    elif menu == '4': # 엄청 큰 소수 입력했을 때 반복문 계속 돌아가는 문제
        numbers = input("Input first second number : ").split()  # 숫자 입력하는 방식 설명해주는 것 개선! n1(space)n2 )    # 가독성 있게 코드 개선 5줄 -> 2줄?
        n1 = int(numbers[0]
        n2 = int(numbers[1])

        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            is_prime = True

            if number < 2:
                pass
            else:
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False  # remove +
                        break  # break 없으면 계속 돌아감
                if is_prime: print(number, end=' ')
        print()


    elif menu == '5':
        print('Terminate Program.')
        break

    else:

        print("Invalid Menu")