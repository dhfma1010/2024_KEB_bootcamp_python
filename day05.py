# inner function
# def out_func(nout):
#     def inner_func(nin):
#         return nin * nin
#     return inner_func(nout)
#
# print(out_func(5))

# closure function   # 다른 언어에서 보기 힘듦
def out_func(nout):
    def inner_func():
        return nout * nout
    return inner_func

x = out_func(9)
print(type(x))
print(x) # 함수 메모리 주소
print(x()) # 함수 실행