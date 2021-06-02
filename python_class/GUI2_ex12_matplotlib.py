import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

fig = Figure(figsize=(10,10), facecolor='white')

axis = fig.add_subplot(111)

xValues=[1,2,3,4]
yValues0=[6,8,7,5]
yValues1=[1,2,3,4]
yValues2=[7.5,1,6,7]

axis.set_xlabel('x label')
axis.set_ylabel('y label')

#범례 달기
lg0, = axis.plot(xValues, yValues0)
lg1, = axis.plot(xValues, yValues1)
lg2, = axis.plot(xValues, yValues2)

axis.grid(linestyle='-') #solild 스타일의 그리드를 그린다.

#범례 설정
fig.legend((lg0, lg1, lg2),("Test1", "Test2", "Test3"), "upper left")

win=tk.Tk()
win.title("Chart Multi")

canvas = FigureCanvasTkAgg(fig, master=win)
canvas._tkcanvas.pack(side='top', fill='both', expand=True)

win.mainloop()
