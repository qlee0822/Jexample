# all() : return True or False
# 반복 가능한(iterable) 자료형 인자로 입력받을 수 있음
# 요소중 하나라도 거짓이면 False
# 요소가 모두 참이면 True


print("all([1, 2, 3, 4, 5, 0]) :", all([1, 2, 3, 4, 5, 0]))  #False
print("all([1, 2, 3, 4, 5]) :", all([1, 2, 3, 4, 5]))     #True
print("all([-1]) :", all([-1]))                #True
print("all([]) :", all([]))                  #True

#######################################################
# any() : return True or False
# 요소중 하나라도 참이면 True
# 요소가 모두 거짓이면 False
print("any([1, 2, 3, 4, 5, 0]) :", any([1, 2, 3, 4, 5, 0]))  #True
print("any([-1]) :", any([-1]))                #True
print("any([]) :", any([]))                  #False
print("any([0]) :", any([0]))                  #False
print('any([0, ""]) :', any([0, ""]))                  #False

#######################################################
#ord : 문자의 아스크 코드 값출력
print(ord('a'))
#chr() 아스키코드 => 해당 문자로 출력
print(chr(97))

#######################################################
#dir
# 해당 객체가 가지고 있는 변수, 함수를 출력
a = [1, 2, 3,]
print(dir(a))

#######################################################
#enumerate(): 열거하다
#리스트, 튜플, 문자열 등의 순서있는 자료형을 인자로 넘겨주면 인덱스 값과 값을 출력
#보통 반복문과 함께 쓰임

lst = ['lion', 'tiger', 'bear', 'hippo']

for i, lstName in enumerate(lst):
    print(i, lstName)

