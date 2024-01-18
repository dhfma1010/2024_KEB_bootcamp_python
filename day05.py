def my_range(first=0, last=5, step=1):
    number = first
    while number < last:
        yield number  # generate return 대신 yield
        number += step

r = my_range()
print(r, type(r))

for x in r:
    print(x)

for x in r:
    print(x)  # 한번 쓰면 쓰고 사라짐. 기억할 공간x , 반복문 반응x


