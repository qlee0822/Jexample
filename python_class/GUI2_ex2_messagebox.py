#tkMessageBox
#tkMessageBox Method
#showinfo(), showwarning(), showerror(), askquestion()
#askokcancel(), askyesno(), askretrycancel()
import tkinter as tk
from tkinter import messagebox as msg

win=tk.Tk()
win.withdraw() # 메시지 창만 독립적으로 사용
msg.showinfo("showinfo", "showinfo Test")
# win.title("Message Test")
# win.geometry("640x400")
# win.resizable(False, False)
#
# def btn1_click():
#     msg.showinfo("showinfo", "showinfo Test")
#
# def btn2_click():
#     msg.showwarning("showwarning", "showwarning Test")
#
# def btn3_click():
#     msg.showerror("showerror", "showerror Test")
#
# def btn4_click():
#     msg.askquestion("askquestion", "askquestion Test")
#
# def askokcancel_msg():
#     msg.askokcancel("askokcancel", "askokcancel Test")
#
# def askyesno_msg():
#     msg.askyesno("askyesno", "askyesno Test")
#
# def askretrycancel_msg():
#     msg.askretrycancel("askretrycancel", "askretrycancel Test")
#
# btn1 = tk.Button(win, text='showinfo()', command=btn1_click)
# btn1.pack(side='left')
# btn2 = tk.Button(win, text='showwarning()', command=btn2_click)
# btn2.pack(side='left')
# btn3 = tk.Button(win, text='showerror()', command=btn3_click)
# btn3.pack(side='left')
# btn4 = tk.Button(win, text='askquestion()', command=btn4_click)
# btn4.pack(side='left')
#
# menu_bar = tk.Menu(win)
# help_menu = tk.Menu(menu_bar, tearoff=0)
# help_menu.add_command(label="askokcancel", command=askokcancel_msg)
# help_menu.add_command(label="askyesno", command=askyesno_msg)
# help_menu.add_command(label="askretrycancel", command=askretrycancel_msg)
# help_menu.add_separator()
# help_menu.add_command(label="exit", command=win.quit)
# menu_bar.add_cascade(label="help", menu=help_menu)
# win.config(menu = menu_bar)

win.mainloop()