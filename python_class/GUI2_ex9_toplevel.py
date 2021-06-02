try:
    #python 2
    import Tkinter as tk
except ImportError:
    #python 3
    import tkinter as tk

win = tk.Tk()
win.title("Toplevel Test")
#geometry(가로폭 x 세로폭 + x좌표 + y좌표)
win.geometry("600x400+200+200")
win.resizable(False, False)
win.config(bg='blue')

win2 = tk.Toplevel()
win2.title("Children Windows")
win2.geometry("600x200")
win2.resizable(False, False)
win2.config(bg='gold', state='iconic')
win2.lift(aboveThis=win)

def lift_win():
    win2.lift(aboveThis=win)

def lower_win():
    win2.lower()

btn1 = tk.Button(win2, text="위로", command=lift_win)
btn2 = tk.Button(win2, text="아래로", command=lower_win)

btn1.pack(padx=30, pady=30)
btn2.pack(padx=30, pady=30)

win.mainloop()



