import tkinter as tk
from tkinter import ttk

#체크 버튼(check button)

win = tk.Tk()
win.title("Check Button Test")

# ent1 = tk.Entry(win, width=50)
# ent1.grid(column=0, row=0)
#
# ent2 = tk.Entry(win, width=50)
# ent2.grid(column=1, row=0)
#
# #Checkbutton 상태 select: 1, deselect: 0
# #sticky: 고정속성, tk.W (왼쪽), tk.E (오른쪽)
# chk1 = tk.Checkbutton(win, text="독서", state='disable')
# #chk1.select()
# chk1.deselect()
# chk1.grid(column=0, row=1, sticky='e')
#
# chk2 = tk.Checkbutton(win, text="운동")
# chk2.select()
# chk2.grid(column=1, row=1, sticky="WE")
#
# chk3 = tk.Checkbutton(win, text="영화감상")
# chk3.grid(column=2, row=1, sticky="NEWS")
#
# Radiobutton
def clickMe():
    print(rdColor.get())

def sel_radio_btn():
    print(rdColor.get())
    rdValue =  rdColor.get()
    if rdValue == 1:
        win.configure(background=Color1)
    elif rdValue == 2:
        win.configure(background=Color2)
    elif rdValue == 3:
        win.configure(background=Color3)


Color1 = "Blue"
Color2 = "Yellow"
Color3 = "Red"
rdColor = tk.IntVar()
rad1 = tk.Radiobutton(win, text="사과", value=1, variable=rdColor, command=sel_radio_btn)
rad1.grid(column=0, row=0)

rad2 = tk.Radiobutton(win, text="딸기", value=2, variable=rdColor, command=sel_radio_btn)
rad2.grid(column=1, row=0)

rad3 = tk.Radiobutton(win, text="오징어", value=3, variable=rdColor, command=sel_radio_btn)
rad3.grid(column=2, row=0)

btn1 = tk.Button(win, text="확인", command=clickMe)
btn1.grid(column=3, row=0)


win.mainloop()