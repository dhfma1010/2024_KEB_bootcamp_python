# preview
subjects = "python c++ database linux"
subject = input("수강신청 과목 입력 : ")

try:
    print(f"해당 과목은 존재합니다. 위치는 {subjects.index(subject)}번 인덱스")

except ValueError:
    print('해당 과목이 존재하지 않습니다.')