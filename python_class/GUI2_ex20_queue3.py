import tkinter
import time
import threading
import queue
import random

#메일이 왔다는 가상의 메일함
class Mailbox(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q
        self.num = 0
        self.arrivalMail = 0

    def run(self):
        while True:
            time.sleep(1)
            if random.randint(1, 5) == 3:
                self.num = random.randint(1, 100)
                self.q.put(self.num)
#메일 도착 알림 코드
class MyApp(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        label_0 = tkinter.Label(self, text="메일도착").grid(row=0, column=0, padx=10, pady=20)

        self.lb_var = tkinter.IntVar(self, 0)
        self.label = tkinter.Label(self, textvariable = self.lb_var)
        self.label.grid(row=0, column=1, padx=20, pady=20)
        self.btn = tkinter.Button(self, text="메일 체크 시작", command=self.start_mailbox)
        self.btn.grid(row=1, columnspan=2, padx=20, pady=20)
        self.mailbox=[]
        self.q = queue.Queue(10)



    def start_mailbox(self):
        Mailbox(self.q).start()
        self.after(0, self.check_Mailbox)

    def check_Mailbox(self):
        try:
            for i in range(0,10):
                arrivalMail = self.q.get(block=False)
                self.mailbox.append(arrivalMail)
                self.lb_var.set(self.mailbox)
        except queue.Empty:
            pass
        finally:
            self.after(3000, self.check_Mailbox)

win = MyApp()
win.mainloop()
