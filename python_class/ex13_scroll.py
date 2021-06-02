import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("Text/Scrolled Text Test")
# txtComments = tk.Text(win)
# txtComments.grid(column=0, row=0)

colors = ["blue", "yellow", "red"]
rdColor = tk.IntVar()
def selCol():
    rdValue = rdColor.get()
    if rdValue == 0:
        win.configure(background="blue")
    elif  rdValue == 1:
        win.configure(background="yellow")
    elif  rdValue == 2:
        win.configure(background="red")

for col in range(3):
    rad = tk.Radiobutton(win, text=colors[col], variable=rdColor, value=col, command=selCol)
    rad.grid(column=col, row=0, sticky='news')


# rad1 = tk.Radiobutton(win, text="Blue", variable=rdColor, value=1, command=selCol)
# rad1.grid(column=0, row=0, sticky="news")
# rad2 = tk.Radiobutton(win, text="Yellow", variable=rdColor, value=2, command=selCol)
# rad2.grid(column=1, row=0, sticky="news")
# rad3 = tk.Radiobutton(win, text="Red", variable=rdColor, value=3, command=selCol)
# rad3.grid(column=2, row=0, sticky="news")


#wrap = tk.CHAR (기본값: 문자단위 줄바꿈)
#wrap = tk.WORD or 'word' (단어단위 줄바꿈)
txtscroll = scrolledtext.ScrolledText(win, width=30, height=4, wrap='word')
txtscroll.grid(column=0, row=1, columnspan="3")

win.mainloop()