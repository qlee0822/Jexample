#Geometry Manager (위치관리 매니저)
#Tkinter에서는 위젯들을 화면에 배치하는 방식으로 3가지 방식을 사용

#pack : 위젯.pack() 메서드를 사용하여 배치, 불필요한 공간을 없애고 기본값(상하)로 고정
#grid : 위젯.grid() 위젯들을 테이블 레이아웃(격자)에 배치하는 방식 (column, row)
#place : 위젯.place() 위젯을 절대 좌표로 정하여 사용, 윈도우 크기 변경에 따라 위젯들이 변경되지 않는다.

#Frame 위젯: Labelframe, RadiobuttonFrame, CheckButtonFrame


import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("400x400")

lbl = tk.Label(win, text="이름", \
               justify='right', \
               background='yellow',\
               width=40, height=10, \
               bd=1, \
               relief="solid", \
               anchor = 'sw'
    )
lbl.config(text="Hello!! Python 1234567890 abced================")
lbl.config(wraplength=100) #한줄에 들어가는 사이즈 정하기
# lbl.config(width=40)
# lbl.config(justify='right')
# lbl.config(background='yellow')
lbl.pack()

txt = tk.Entry(win)
txt.pack()

btn = tk.Button(win, text="확인")
btn.pack()





win.mainloop()