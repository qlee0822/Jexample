import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("640x400")

menuBar = tk.Menu(win, tearoff=0)
menu1 = tk.Menu(win, tearoff=0)
submenu = tk.Menu(win, tearoff=0)
submenu.add_radiobutton(label='option1')
submenu.add_radiobutton(label='option2')

menuBar.add_cascade(label='Menu 1', menu=menu1)
menu1.add_cascade(label='SubMenu', menu=submenu)

win.config(menu = menuBar)

win.mainloop()