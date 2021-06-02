import tkinter as tk
from tkinter import ttk

#pack Parameter
#side : top(default), bottom, left, right
#anchor : center(default), n, e, w, s, ne, nw, se, sw
#fill : none(default), x, y, both
#expand : False(default), True
#padx : 위젯에 대한 x 방향으로 외부패딩
#ipadx : 위젯에 대한 x 방향으로 내부패딩
#pady : 위젯에 대한 y 방향으로 외부패딩
#ipady : 위젯에 대한 y 방향으로 내부패딩
#pack()은 grid와는 같이 사용할 수 없다. 하지만 place와는 같이 사용 가능

win = tk.Tk()
win.geometry("640x400")
win.resizable(False, False)
win.title("Pack Test")
win.configure(bg='yellow')

btn1 = tk.Button(win, text="top")
btn1_1 = tk.Button(win, text='top-1')

btn1.pack(side='top')
btn1_1.pack(side='top', fill='x')

btn2 = tk.Button(win, text="bottom")
btn2_1 = tk.Button(win, text='bottom-1')

btn2.pack(side='bottom',  anchor='e')
btn2_1.pack(side='bottom', fill='x')

btn3 = tk.Button(win, text="left")
btn3_1 = tk.Button(win, text='left-1')

btn3.pack(side='left',  anchor='sw')
btn3_1.pack(side='left', fill='y')

btn4 = tk.Button(win, text="right")
btn4_1 = tk.Button(win, text='right-1')

btn4.pack(side='right',  anchor='nw')
btn4_1.pack(side='right', fill='y')

btn5 = tk.Button(win, text="center", bg='red')
btn5.pack(fill='both', expand=True)

win.mainloop()