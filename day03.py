# prime number
number = int(input("Input number : "))

cnt = 0
i = 2
while i < number:
    if number % i == 0:
        cnt = cnt + 1
        break  # break 없으면 계속 돌아감
    print(i, end=' ')   #몇 번 도는지 확인용
    i = i + 1

if cnt == 0:
    print(f'{number} is prime number')
else:
    print(f'{number} is NOT prime number!')






