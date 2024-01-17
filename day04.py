subjects = ["데이터베이스","C++", '5', "Java", "Python", "Java", '9', "리눅스"]

print(subjects)
subjects.sort()  # 문자와 정수 타입 비교 불가  --> 방법 int를 str로 바꿔줌 # 우선순위 : 숫자문자열, 알파벳, 한글
print(subjects)
subjects.sort(reverse=True) # desc
print(subjects)

print()
copy_subjects = sorted(subjects)
print(subjects)
print(copy_subjects)
