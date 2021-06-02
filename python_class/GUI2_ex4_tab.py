import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st

win=tk.Tk()
win.title("Tab Test2")
win.geometry("640x400")
win.resizable(False, False)

def fruitSel():
    insertText = "{}을(를) {}개 선택하셨습니다.".format(entVar1.get(), number.get())
    scr.insert(tk.INSERT, insertText)

tabControl = ttk.Notebook(win)
tabControl.pack(expand=True, fill="both", padx=10, pady=10)

#첫번째 탭
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Tab 1")

#두번째 탭
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")

lbFrame = ttk.LabelFrame(tab1, text="Label Frame1")
lbFrame.grid(row=0, column=0, padx=8, pady=5)

lb1 = ttk.Label(lbFrame, text="과일명 입력")
lb1.grid(row=0, column=0, sticky='w')

entVar1 = tk.StringVar()
ent1 = ttk.Entry(lbFrame, width=10, textvariable=entVar1)
ent1.grid(row=1, column=0, sticky='w', padx=5, pady=5)

ttk.Label(lbFrame, text="수량").grid(row=0, column=1, sticky='w')

number = tk.StringVar()
numCombo = ttk.Combobox(lbFrame, width=10, textvariable=number)
numCombo['values'] = (0, 1, 2, 3, 4, 5)
numCombo.current(0)
numCombo.grid(row=1, column=1, padx=5, pady=5)

btn1 = ttk.Button(lbFrame, text="확인", command = fruitSel)
btn1.grid(row=1, column=2, sticky='w', padx=5, pady=5)

scr = st.ScrolledText(lbFrame, width=30, height=3, wrap=tk.WORD)
scr.grid(row=3, columnspan=3, sticky='news', padx=5, pady=5)

# Tab 2 --------------------------------------------------------------

lbFrame2 = ttk.LabelFrame(tab2, text="Label Frame2")
lbFrame2.grid(row=0, column=0, padx=10, pady=10)

chkVar1 = tk.IntVar()
chk2_1 = tk.Checkbutton(lbFrame2, text="Check 2_1", variable=chkVar1)
chk2_1.select()
chk2_1.grid(row=0, column=0, sticky="w", padx=5, pady=5)

chkVar2 = tk.IntVar()
chk2_2 = tk.Checkbutton(lbFrame2, text="Check 2_2", variable=chkVar2)
chk2_2.deselect()
chk2_2.grid(row=0, column=1, sticky="w", padx=5, pady=5)

chkVar3 = tk.IntVar()
chk2_3 = tk.Checkbutton(lbFrame2, text="Check 2_3", variable=chkVar3)
chk2_3.deselect()
chk2_3.grid(row=0, column=2, sticky="w", padx=5, pady=5)

def rdFunc():
    rdSel = rdVar.get()
    win.configure(bg=colors[rdSel])
    lbFrames.configure(text=colors[rdSel])
    # if rdSel == 0: lbFrames.configure(text="Red")
    # if rdSel == 1: lbFrames.configure(text="Yellow")
    # if rdSel == 2: lbFrames.configure(text="Blue")


rdVar = tk.IntVar()
colors = ['Red', 'Yellow', 'Blue']
for col in range(3):
    rad = tk.Radiobutton(lbFrame2, text=colors[col], variable = rdVar, value=col, command=rdFunc)
    rad.grid(row=1, column=col, sticky="w", padx=5, pady=5)

lbFrames = ttk.LabelFrame(lbFrame2, text = "Label 프레임")
lbFrames.grid(row=2, columnspan=3, sticky="news", padx=5, pady=5)

ttk.Label(lbFrames, text="Label 3").grid(row=0, column=0, sticky="w", padx=5, pady=5)
ttk.Label(lbFrames, text="Label 4").grid(row=1, column=0, sticky="w", padx=5, pady=5)
ttk.Label(lbFrames, text="Label 5").grid(row=2, column=0, sticky="w", padx=5, pady=5)

win.mainloop()