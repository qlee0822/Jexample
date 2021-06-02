import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("ComboBox Test")

def select():
    lb2.configure(text="{}을(를) {}개 구매하겠습니다.".format(fruitName.get(), combostr.get()))

ttk.Label(win, text="과일명 입력 : ").grid(column=0, row=0)

fruitName = tk.StringVar()
fruitEntry = ttk.Entry(win, width=15, textvariable=fruitName)
fruitEntry.grid(column=0, row=1, sticky="NEWS")

ttk.Label(win, text="수량 선택 : ").grid(column=1, row=0)

combostr = tk.StringVar()
combo1 = ttk.Combobox(win, width=10, textvariable=combostr) # textvariable 선택된 데이터
combo1.grid(column = 1, row = 1, sticky="NEWS")
combo1['values'] = ("5", "10", "15", "20")

btn1 = ttk.Button(win, text="확인", command=select)
btn1.grid(column=2, row=1, sticky="NEWS")

lb2 = ttk.Label(win, text="")
lb2.grid(column=1, row=2)

fruitEntry.focus()

win.mainloop()