#Spinbox 위젯

import tkinter as tk
from tkinter import scrolledtext
win = tk.Tk()
win.title("Spinbox Test")
win.geometry("600x400")
win.resizable(False, False)
#bd(borderwidth)
# relief 속성값: flat, sunken, raised, groove, ridge, solid

def _spin():
    val = spin.get()
    print(val)
    scrol.insert(tk.INSERT, str(val) + '\n')

def _spin1():
    val = spin1.get()
    print(val)
    scrol.insert(tk.INSERT, str(val) + '\n')

spin = tk.Spinbox(win, from_=0, to=10, width=5, bd=8, relief='flat', command=_spin)
spin1 = tk.Spinbox(win, values=(10,20,40,100,200), width=5, bd=8, relief='sunken', command=_spin1)
spin2 = tk.Spinbox(win, from_=0, to=10, width=5, bd=8, relief='raised')
spin3 = tk.Spinbox(win, from_=0, to=10, width=5, bd=8, relief='groove')
spin4 = tk.Spinbox(win, from_=0, to=10, width=5, bd=8, relief='ridge')
spin5 = tk.Spinbox(win, from_=0, to=10, width=5, bd=8, relief='solid')
spin.grid(row=0, column=0, padx=20, pady=20)
spin1.grid(row=0, column=1, padx=20, pady=20)
spin2.grid(row=1, column=0, padx=20, pady=20)
spin3.grid(row=1, column=1, padx=20, pady=20)
spin4.grid(row=2, column=0, padx=20, pady=20)
spin5.grid(row=2, column=1, padx=20, pady=20)

scrol = scrolledtext.ScrolledText(win, width=30, height=10, wrap=tk.WORD)
scrol.grid(row=3, columnspan=2, sticky='we', padx=20, pady=20)

win.mainloop()