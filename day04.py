
numbers = input("Input first second number : ").split()  # 숫자 입력하는 방식 설명해주는 것 개선! n1(space)n2 )    # 가독성 있게 코드 개선 5줄 -> 2줄?
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

for number in range(n1, n2 + 1):
    is_prime = True

    if number < 2:
        pass
    else: # 소수일 때 for문 너무 많이 돌아감
        i = 2
        while i*i < number: # 반복횟수 감소 ################# 성능 개선 코드 , performance issue
            if number % i == 0:
                is_prime = False  # remove +
                break  # break 없으면 계속 돌아감
            i = i + 1
            # print(i, end =' ') 몇번 반복하는지 확인
        if is_prime:
            pass
            print(number, end=' ')
print()
