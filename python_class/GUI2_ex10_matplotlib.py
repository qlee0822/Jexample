import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

fig = Figure(figsize=(10,10), facecolor='white')

# axis = fig.add_subplot(111) #1행, 1열에 첫번째 그래프
axis = fig.add_subplot(211) #1행, 1열에 첫번째 그래프

xValues = [1,2,3,4]
yValues = [5,8,7,6]

axis.plot(xValues, yValues)
axis.set_xlabel("x Label")
axis.set_ylabel("y Label")
axis.grid(linestyle='-') #solild 스타일의 그리드를 그린다.

axis2 = fig.add_subplot(212) #2행,1열에 두번째 그래프
xValues = [1,2,3,4]
yValues = [7,5,8,6]
axis2.plot(xValues, yValues)
axis2.set_xlabel("x Label2")
axis2.set_ylabel("y Label2")
axis2.grid(linestyle='-') #solild 스타일의 그리드를 그린다.

win = tk.Tk()
canvas = FigureCanvasTkAgg(fig, master=win)
canvas._tkcanvas.pack(side=tk.TOP, fill='both', expand=True)

win.mainloop()