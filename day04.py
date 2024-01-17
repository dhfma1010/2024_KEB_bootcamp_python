# subjects = ["a", "b", "c"] # b,c,d 값 바뀌지 x(immutable한 값 )
import copy

subjects = ["a",["b","c"], "d"] #  vs list (mutable한 값이라 복제한 것도 다 변화)
a = subjects
b = subjects.copy()
c = list(subjects)
d = subjects[:]
e = copy.deepcopy(a)
print(subjects, a, b, c, d, e)
subjects[1][1]= "x"
print(subjects, a, b, c, d, e)

