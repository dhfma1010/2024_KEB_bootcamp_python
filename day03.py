univ = "inha"

i = 0 # 초기값 오류 문제 , 초기값 조정하면 특정 구간 뽑을 수 있음
while i < len(univ):
    print(univ[i], end=' ')
    i = i + 1  # 연산 오류 문제

print()

for letter in univ:  # 오류 적음 , 특정 구간 뽑으려 하면 안됨
    print(letter, end=' ')

print()

# for k in range(0, len(univ), 1):  # 시작, 끝값, 증감 입력 오류 문제
# for k in range(0, len(univ)):
for k in range(len(univ)):
    print(univ[k], end=' ')
