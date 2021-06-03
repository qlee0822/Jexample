#input()
# 사용자 입력을 받음

# a = input("Enter the Number : ")
#
# print(type(a))
# print(a)

#isinstance()
#첫번째 인수 --> 인스턴스
#두번째인수 --> 클래스 이름
#해당 클래스의 인스턴스 여부 반환 (True, False)

class Test:
    pass

a = Test()
print(type(a))

print(isinstance(a, Test))

x = [1,2,3,4,5]
print(type(x))

y = (1,2,3,4,5) # list
z = 1, 2, 3, 4, 5
print(type(y)) # tuple
print(type(z)) # tuple


#sum
#넘겨받은 리스트, 튜블의 모든 요소의 합 반환
print(sum(x))
print(sum(y))

#zip()
#동일개수의 자료형을 묶음

a = [1, 2, 3, 4, 5]
b = ['a', 'b','c','d','e']

print(zip(a, b))
print(list(zip(a, b)))

c = ['a','b','c']
d = [1,2,3,4]
print(list(zip(c, d)))

#pow()
#제곱한 값을 반환
print(pow(2,4))
a = 2**4
pow(2, 4)