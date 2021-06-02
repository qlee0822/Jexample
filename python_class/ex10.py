import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Test")

def cilckMe():
    #lb2.configure(text="하이!!")
    lb2.configure(text= "하이!! " + id.get())
    btn1.configure(state='disabled')
    id.set("더 이상 입력 안됨") # id값을 새롭게 지정
    entry1.configure(state='disabled')
    #entry1.delete(0, )

lb1 = tk.Label(win, text="아이디")
lb1.grid(column=0, row=0)

id = tk.StringVar()
entry1 = tk.Entry(win, textvariable = id)
entry1.grid(column=1, row=0)

btn1 = tk.Button(win, text="클릭", command=cilckMe)
btn1.grid(column=2, row=0)

lb2 = tk.Label(win, text="")
lb2.grid(column=1, row=1)

entry1.focus() # 포커스 설정하기

win.mainloop()