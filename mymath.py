print(globals())

if __name__ == "__main__":

    while True:
        menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Prime1   4) Prime2   5) Quit program : ")

        if menu == '1':
            fahrenheit = float(input('Input Fahrenheit : '))
            print(f'Fahrenheit : {fahrenheit}F, Celsius : {mm.fahrenheit_to_celsius(fahrenheit):.4f}C')
        elif menu == '2':
            celsius = float(input('Input Celsius : '))
            print(f'Celsius : {celsius}C, Fahrenheit : {mm.celsius_to_fahrenheit(celsius):.4f}F')
        elif menu == '3':
            number = int(input("Input number : "))
            if mm.isprime(number):
                print(f'{number} is prime number')
            else:
                print(f'{number} is NOT prime number!')
        elif menu == '4':
            numbers = input("Input first second number : ").split()
            n1 = int(numbers[0])
            n2 = int(numbers[1])

            if n1 > n2:
                n1, n2 = n2, n1

            for number in range(n1, n2 + 1):
                if isprime(number):
                    print(number, end=' ')
            print()
        elif menu == '5':
            print('Terminate Program.')
            break
        else:
            print('Invalid Menu!')

else:
    print("mymath is not a main file")





def isprime(n) -> bool:
    """
    A function that returns as a boolean whether the number passed as a parameter is a prime number.
    :param n: Parameter to judge
    :return: True if prime number, False if not prime number.
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


def fahrenheit_to_celsius(fahrenheit) -> float:
    """
    Function to convert Fahrenheit temperature to Celsius temperature
    :param fahrenheit:
    :return: celsius temperature
    """
    return (fahrenheit - 32.0) * 5.0 / 9.0





def celsius_to_fahrenheit(celsius) -> float:
    """
    Function to convert Celsius temperature to Fahrenheit temperature
    :param celsius:
    :return: fahrenheit temperature
    """
    return (celsius*9.0/5.0)+32.0