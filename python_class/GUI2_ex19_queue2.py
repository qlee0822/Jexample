# Queue, LifoQueue, PriorityQueue 비교
# 입력방법은 동일 하나, 내부 정렬방식의 차이가 있기 때문에 출력시 순서가 다름

import queue

# 큐객체에 있는 아이템을 출력해주는 함수
def Get_item(q):
    get_items = []
    n = q.qsize()
    while n>0:
        get_items.append(q.get())
        n -= 1
    return get_items

# Queue 객체
itemStr = '밤,호두,땅콩'
q = queue.Queue()

for i in itemStr.split(','):
    q.put(i)

x = Get_item(q)
print(x)

q2 = queue.LifoQueue()
for i in itemStr.split(','):
    q2.put(i)

x = Get_item(q2)
print(x)

q3 = queue.PriorityQueue()
q3.put((7,'밤'))
q3.put((9,'호두'))
q3.put((2,'땅콩'))
# for i in itemStr.split(','):
#     q3.put(i)

x = Get_item(q3)
print(x)
