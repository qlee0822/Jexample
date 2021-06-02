# queue Module : 스레드 환경을 생각하고 만들어졌음
# 여러 스레드 객체들을 동시에 큐객체(Queue, PriorityQueue, LifoQueue)에 데이터를
# 입력하고, 데이터를 출력하여도 정상적으로 작동
# 파이썬에서는 queue 모듈에서 Queue, PriorityQueue(우선순위큐), 스택(LifoQueue)을 제공

# queue.Queue(maxsize): 선입선출(FIFO: First-in, First-Out) 큐 객체를 생성
# queue.LifoQueue(maxsize): 일반적인 스텍(Stack)과 같은 후입선출(LIFO Last-in, First-Out) 큐객체를 생성
# queue.PriorityQueue(maxsize): 우선순위 큐 객체를 생성, 입력되는 아이템의 형식은 튜플로 입력
#                               우선순위는 숫자가 작을 수록 높은 순위
# maxsize: 저장할 수 있는 최대 아이템 개수

# queue Method
# qsize(): 큐 객체에 입력된 아이템의 개수
# put(): 큐에 아이템을 입력
# put_nowait(item): 블로킹없이 큐 객체에 아이템을 입력, 데이터가 꽉 차있을 경우 queue.Full 예외 발생
# get(): 아이템 1개를 반환
# get_nowait(): 블로킹없이 큐 객체에 있는 아이템을 반환, 데이터가 없는 경우 queue.Empty 예외 발생

import queue

q = queue.Queue()
q.put("사과")
q.put("오렌지")
q.put("바나나")
q.put(10)
num = q.qsize()
print(num)

data = q.get()
print(data)

q2 = queue.Queue(2) # 아이템이 두개만 저장
q2.put("호두")
q2.put("밤")
#q2.put("땅콩") #다른 쓰레드가 아이템을 가지고 갈 때까지 무한 대기 (blocking)
#Queue가 비어 있는 상태에서 get()호출하면 Queue객체는 블로킹(blacking) 됨

#위의 코드에서 무한대기 상태를 피하고자 put_nowait(), get_nowait()을 지원
q3 = queue.Queue(2)
q3.put_nowait("1")
q3.put_nowait("2")
#q3.put_nowait("3") #큐가 차있으면 예외 발생

q3.get_nowait()
q3.get_nowait()
#q3.get_nowait() #큐가 비어있으면 예외 발생

# put(), get() 메서드에 인자를 사용할 수 있음. put(item, block유무, timeout)
q4 = queue.Queue(2)
q4.put("밤")
q4.put("호두")
#q4.put("땅콩", True, 5) #5초간 대기(블러킹) 후 예외 발생
q4.put("땅콩", False) #예외 발생 = put_nowait()