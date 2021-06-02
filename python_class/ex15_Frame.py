import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("640x400")
win.resizable(False, False)
win.title("Frame Test")

frame1 = tk.Frame(win, bd=2, relief='solid', bg='yellow')
frame1.pack(fill='both', expand=True, side='left', padx=10, pady=10)

frame2 = tk.Frame(win, bd=2, relief='solid', bg='red')
frame2.pack(fill='both', expand=True, side='right', padx=10, pady=10)

btn1 = tk.Button(frame1, text='프레임1')
btn1.pack(side='right')

btn2 = tk.Button(frame2, text='frame2 button')
btn2.pack(fill='both')

win.mainloop()