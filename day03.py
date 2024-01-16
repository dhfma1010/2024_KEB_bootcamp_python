# prime number
number = int(input("Input number : "))
is_prime = True # int -> bool

if number < 2:
    print(f'{number} is NOT prime number!')
else:
    i = 2
    while i < number:
        if number % i == 0:
            is_prime = False # remove +
            break  # break 없으면 계속 돌아감
        i = i + 1

    # if cnt ==0:
    if is_prime: # remove ==
        print(f'{number} is prime number')
    else:
        print(f'{number} is NOT prime number!')





