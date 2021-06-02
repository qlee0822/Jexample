#리턴 값이 있는 함수

def my_func_rtn(x,y):
    return x+y

print(my_func_rtn(5, 3))

result = my_func_rtn(5, 3)
print(result)

# 숫자 이외의 자료형을 매개변수로
animals = ['사자', '호랑이', '늑대', '여우']
def show_list_element(ani):
    for x in ani:
        print(x)

show_list_element(animals)

# 숫자 이외의 자료형 리턴도 가능
def my_func_list_rtn():
    return ['a','b','c','d']

print(my_func_list_rtn())

result = my_func_rtn(5, 3)
print(pow(result, 3))

show_list_element(my_func_list_rtn())