import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

fig = Figure(figsize=(10,10), facecolor='white')
xValues = [1,2,3,4]
yValues = [5,8,7,6]

axis1 = fig.add_subplot(221)
axis2 = fig.add_subplot(222, sharex=axis1, sharey=axis1)
axis3 = fig.add_subplot(223, sharex=axis1, sharey=axis1)
axis4 = fig.add_subplot(224, sharex=axis1, sharey=axis1)

axis1.plot(xValues, yValues)
axis1.set_xlabel("x Label 1")
axis1.set_ylabel("y Label 1")
axis1.grid(linestyle='-') #solild 스타일의 그리드를 그린다.

axis2.plot(xValues, yValues)
axis2.set_xlabel("x Label 2")
axis2.set_ylabel("y Label 2")
axis2.grid(linestyle='-') #solild 스타일의 그리드를 그린다.

axis3.plot(xValues, yValues)
axis3.set_xlabel("x Label 3")
axis3.set_ylabel("y Label 3")
axis3.grid(linestyle='-') #solild 스타일의 그리드를 그린다.

axis4.plot(xValues, yValues)
axis4.set_xlabel("x Label 4")
axis4.set_ylabel("y Label 4")
axis4.grid(linestyle='-') #solild 스타일의 그리드를 그린다.

win = tk.Tk()
win.title("Chart in Tk with matplotlib...")
canvas = FigureCanvasTkAgg(fig, master=win)
canvas._tkcanvas.pack(side='top', fill='both', expand=True)
win.mainloop()