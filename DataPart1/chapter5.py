#짝수 구구단을 출력

def gugudan2(n):
    for x in range(n, 10, 2):
        for i in range(1, 10):
            print("{} x {} = {}".format(x, i, x*i), end='\t')
        print()

gugudan2(2)