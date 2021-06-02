import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("640x400")
win.resizable(True, True)
win.title("MenuButton Test")
win.configure(bg='yellow')

#Menu Button
# tkinter.Menubutton(윈도우창,...) 클래스를 이용헤서 메뉴버튼의 속성 설정 후 Menu 클래스를 이용해서 메뉴 속성 설정
# Menubutton과 Menu 연결

# Menubutton Parameter
# text: 메뉴버튼에 표시할 문자열
# textvariable: 메뉴버튼에 표시할 문자열을 가져 올 변수
# anchor, justify
# wraplength: 자동 줄바꿈 너비 설정

def cls():
    win.quit()

menubutton=tk.Menubutton(win,text="메뉴버튼", relief="ridge", direction="right")
menubutton.pack(side='left', padx=10, pady=10)

menu=tk.Menu(menubutton, tearoff=0)
menu.add_command(label="하위메뉴-1")
menu.add_command(label="하위메뉴-2")
menu.add_command(label="하위메뉴-3", command=cls)

chkVar1 = tk.IntVar()
chkVar2 = tk.IntVar()
menu.add_separator()
menu.add_checkbutton(label='check1', variable=chkVar1)
menu.add_checkbutton(label='check2', variable=chkVar2)

menubutton["menu"]=menu

win.mainloop()