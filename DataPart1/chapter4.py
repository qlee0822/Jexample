# 2~9까지의 정수를 하나 입력받아 해당 정수의 단(구구단)을 출력하는 함수를 작성

def gugudan(a):
    for i in range(1,10):
        print("{} x {} = {}".format(a, i, a*i))


gugudan(3)