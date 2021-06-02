# import threading
# import requests
# import time
#
# def getHtml(url):
#     res = requests.get(url)
#     time.sleep(1)
#     print(url, len(res.text), '개의 문자')
#
# thread1 = threading.Thread(target=getHtml, args=('http://www.naver.com',))
# thread1.start()
#
# thread1.join()
#
# print("----- 종료 -----")

import threading, requests, time

class HtmlGetter(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
    def run(self):
        res=requests.get(self.url)
        time.sleep(1)
        print(self.url, len(res.text), '개의 문자')

thread1 = HtmlGetter('http://www.naver.com')
thread1.start()

thread1.join()

print("----- 종료 -----")