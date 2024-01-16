# prime number  # 두 수 사이의 소수 출력

numbers = input("Input first second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

for number in range(n1, n2+1):
    is_prime = True

    if number < 2:
        pass # 자리 차지하는데 그냥 지나감
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False # remove +
                break  # break 없으면 계속 돌아감
        if is_prime: print(number, end=' ')








