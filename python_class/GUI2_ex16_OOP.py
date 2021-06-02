import tkinter as tk
from tkinter import ttk

class MyApp():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("OOP Programing")
        self.win.geometry("600x400+200+200")
        self.win.resizable(False, False)
        self.create_widgets()

    def show(self):
        self.label.configure(text="당신은 " + self.name.get() + ' ' + self.num.get() + "개를 선택했습니다.")

    def create_widgets(self):
        self.name = tk.StringVar()
        entry_name = tk.Entry(self.win, width=10, textvariable=self.name)
        entry_name.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        btn1 = tk.Button(self.win, text="확인", command=self.show)
        btn1.grid(row=1, column=2)

        ttk.Label(self.win, text="과일명").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.win, text="수량 선택").grid(row=0, column=1, padx=10, pady=10)

        self.num = tk.StringVar()
        combo1 = ttk.Combobox(self.win, width=10, textvariable=self.num)
        combo1['values'] = (1, 2, 4, 8, 100, 120)
        combo1.grid(row=1, column=1)

        combo1.current(0)
        self.label = ttk.Label(self.win, text='과일을 선택하세요')
        self.label.grid(row=2, columnspan=2)

#----------------GUI Create... -------------------
myApp = MyApp() #인스턴스(객체) 생성
myApp.win.mainloop()