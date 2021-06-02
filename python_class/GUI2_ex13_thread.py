# 쓰레드(비동기 프로그래밍)
# 비동기 프로그래밍: 서로 간섭없이 독립적으로 작업을 진행하는 프로그램을 개발하는 것
# 비동기 프로그래밍은 독립적인 작업을 만드는 것인데, 독립적인 작업을 만드는 간단한 방법은 Thread를 이용하는 방법

# 파이썬에서 쓰레드를 사용하기 위한 모듈: _thread, threading

import _thread
import time
import random

def DoitThread(str): #함수를 쓰레드 진입점
    cnt = 0
    while(cnt < 10):
        time.sleep(random.randint(0, 100)/300.0)
        print(str, cnt)
        cnt += 1

# _thread.start_new_thread(스레드 진입접, (스레드 진입점에 전달할 인자))

_thread.start_new_thread(DoitThread, ("Thread 1...........",))
_thread.start_new_thread(DoitThread, ("Thread 2...",))

#print("작업을 중지하기 위해서는 아무키나 누르세요.")
#input()