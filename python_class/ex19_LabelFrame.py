import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("640x400")
win.resizable(True, True)
win.title("LabelFrame Test")
win.configure(bg='yellow')

lbFrame = ttk.LabelFrame(win, text="Label Frame1")
lbFrame.grid(column=0, row=0, padx=10, pady=10)

lbFrame1 = ttk.LabelFrame(lbFrame, text="Label Frame2")
lbFrame1.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

name = tk.StringVar()
number = tk.IntVar()
ttk.Label(lbFrame, text="과일명").grid(row=0, column=0)
ttk.Entry(lbFrame, width=12, textvariable=name).grid(row=1, column=0, padx=5, pady=5)

ttk.Label(lbFrame, text="수량").grid(row=0, column=1)
ttk.Entry(lbFrame, width=10, textvariable=number).grid(row=1, column=1, padx=5, pady=5)

ttk.Label(lbFrame1, text="Label1").grid(column=0, row=0, sticky='w')
ttk.Label(lbFrame1, text="Label2").grid(column=1, row=0, sticky='w')
ttk.Label(lbFrame1, text="Label3").grid(column=3, row=0, sticky='w')

#winfo_children(): 자식 목록을 반환하는 함수
for child in lbFrame1.winfo_children():
    child.grid_configure(padx=5, pady=5, ipadx=5, ipady=5)

win.mainloop()