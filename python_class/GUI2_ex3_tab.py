import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("Tab Test")
win.geometry("640x400")
win.resizable(False, False)

#탭컨트롤을 생성하는 메소드 ttk에 Notebook()
tabControl = ttk.Notebook(win)
tabControl.pack(expand=True, fill="both", padx=10, pady=10)

#첫번째 탭
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Tab 1")

#두번째 탭
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")

tk.Label(tab1,text="Tab 1의 라벨입니다.").grid(column=0, row=0, padx=10, pady=10)
tk.Label(tab2,text="Tab 2의 라벨입니다.").grid(column=0, row=0, padx=10, pady=10)

win.mainloop()