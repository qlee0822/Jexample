# eval()
# 문자열을 실행
# 보통 입력받은 문자열을 통해서 함수나 클래스를 통적으로 실행시키고자 할 때 사용
# 보안 문제로 사용하는 것을 권장 X

print(eval('3' + '4'))
print(eval('1+2+3'))

# hex()
# 정수 ==> 16진수(hexadecimal)

print(hex(15))
print(hex(10))

# id()
# 객체 --> 고유 주소 값
obj = 100
print(type(obj))
print(id(obj))
print(id(100))
obj2 = obj
print(id(obj2))

# filter()
# 걸러낸다는 의미
# 첫번째인자 ==> 함수명
# 두번째인자 --> iterable type
# 변환 값이 참만 필터링해서 리턴
def _odd(x):
    result = []
    for i in x:
        if i % 2 == 0:
            result.append(i)
    return result
def _even(x):
    result = []
    for i in x:
        if i % 2 != 0:
            result.append(i)
    return result

lst = [0,1,2,3,4,5,6,7,8,9]

def _odd2(x):
    return x % 2 !=0

print(_odd(lst))
print(_even(lst))

print(list(filter(_odd2, lst)))