# 쓰레드를 생성하는 모듈 Threading 사용하기
# 쓰레드 생성 : threading.Thread() 메소드를 호출
# Thread(target= 쓰레드 진입점, args=전달할 인자(튜플형태)),
# args 대신에 kwargs사용할 경우에는 딕셔너리 행태로
# 쓰레드를 동작 시킬때는 쓰레드 객체의 start 메소드를 사용
# 쓰레드의 종료까지 대기할 때는 join메소드를 호출

import threading
import time
import random

def DoitThread(str): #함수를 쓰레드 진입점
    cnt = 0
    while(cnt < 10):
        time.sleep(random.randint(0, 100)/300.0)
        print(str, cnt)
        cnt += 1

th1 = threading.Thread(target=DoitThread, args=("Thread 1 ......... ",))
th2 = threading.Thread(target=DoitThread, args=("Thread 2 ......... ",))

print('-------------- Thread Start ----------------')

th1.start()
th2.start()

th1.join()
th2.join()

print('-------------- Thread End ----------------')

# threading.Thread 메소드로 만들어지는 방식은 Thread 클래스를 파생하여 쓰레드가 실행할
# run() 메소드를 재정의해서 사용하는 방식. 즉 run()가 쓰레드를 실제로 실행시키는 메소드
# start()가 run()을 호출출