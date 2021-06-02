# Scale 위젯 : 수치조정바
# 생성: Scale(윈도우창, 인수...) 인수(파라미터)를 이용하여 수치조정바의 속성을 설정
# Scale Method
#   set() : 수치 조정바의 값을 변경/설정
#   get() : 수치 조정바의 값을 반환

# Scale Parameter
#   label: 수치 조정바에 표시되는 문자
#   showvalue: 수치 조정바에 값 표시 여부 설정, 기본값(True)

# Scale의 형태 설정
#   width, height, relief, bd, bg
#   troughclor : 수치 조정바의 내부 배경 색상
#   orient :수치 조정바의 표시 방향, 기본값은(vertical), 가로방향으로 horizontal
#   sliderlength : 수치 조정바의 슬라이더 길이, 기본값(30)
#   sliderrelief : 수치 조정바의 슬라이더 테두리 모양(raised)
#   tickinterval : 수치 조정바의 수치 값 간격

#   from : 수치 조정바의 최소값, 기본값(0)
#   to :  수치 조정바의 최대값, 기본값(100)
#   resolution :  수치 조정바의 간격, 기본값(1)

import tkinter as tk

win = tk.Tk()
win.title("Scale Test")
win.geometry("600x400")
win.resizable(False, False)

def showVal(self):
    valStr = "수치 : {}".format(scale.get())
    label.config(text=valStr)


scaVar = tk.IntVar()
# scale 생성
scale = tk.Scale(win, variable=scaVar, showvalue=True, orient='horizontal', tickinterval=50, to=400, length=300,\
                 command=showVal)
scale.pack()

label = tk.Label(win, text="수치 : 0")
label.pack()

win.mainloop()
