# Fahrenheit - Celsius 보완
# 1) while 구문 가장 바깥에 2) else 대신 elif menu==3 ; 3눌러야 quit, 다른 입력값 이면 계속 반복

while True:

    menu = input("1) Fahrenheit -> Celsius 2) Celsius -> Fahrenheit 3) Quit program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0/9.0):.4f}C')
        # menu = input("1) Fahrenheit -> Celsius 2) Celsius -> Fahrenheit 3) Quit program : ") # 이부분 중복

    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius * 9.0/5.0) + 32.0):.4f}F')
        # menu = input("1) Fahrenheit -> Celsius 2) Celsius -> Fahrenheit 3) Quit program : ") # 이부분 중복 --> while문 제일 바깥에 써야

    elif menu == '3':
        print('Terminate Program.')
        break