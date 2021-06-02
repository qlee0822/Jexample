import tkinter
from datetime import datetime
import tkinter.font

class MyApp(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.lb_Var = tkinter.StringVar(self, 0)
        self.font=tkinter.font.Font(family="맑은 고딕", size=20)
        self.label = tkinter.Label(self, textvariable=self.lb_Var, font=self.font)
        self.label.pack()

    def timer(self):
        # while True:
        #     time.sleep(1)
        #     self.lb_Var.set(self.lb_Var.get()+1)
        self.lb_Var.set(datetime.now())
        #print(datetime.now())
        self.after(1000, self.timer) #독립적인 하나의 쓰레드를 만듦
win = MyApp()
win.timer()
win.geometry('600x400')
win.mainloop()