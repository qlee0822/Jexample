import tkinter as tk
from tkinter import ttk

#width, height
#relwidth:위젯의 너비 비율(0~1)
#relheight:위젯의 높이 비율(0~1)
#relx: x좌표의 배치 비율(0~1)
#rely: y좌표의 배치 비율(0~1)
#anchor: nw(기본값), n, e, w, s,nw, ne, sw,se

win = tk.Tk()
win.geometry("640x400")
win.resizable(True, True)
win.title("Place Test")
win.configure(bg='yellow')

btn1 = tk.Button(win, text="(100,100)")
btn1.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)

btn2 = tk.Button(win, text="테스트", bg='red')
btn2.place(x=100, y=100, anchor='sw', width=80, height=80)

win.mainloop()