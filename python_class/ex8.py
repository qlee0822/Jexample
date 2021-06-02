# Tkinter 주요 위젯
# Button        버튼
# Label         텍스트 또는 이미지 표시
# CheckButton   체크박스
# Entry         단순한 라인 텍스트 박스
# ListBox       리스트 박스
# RadioButton   옵션 버튼
# Message       Label과 비슷하게 텍스트 표시, Label과 다르게 자동 래핑 가능
# Scale         슬라이스바
# Scrollbar     스트롤바
# Text          멀티라인을 제공하는 텍스트 박스
# Menu          메뉴
# Menubutton    메뉴 버튼
# Toplevel      새로운 윈도우를 생성할 때 사용 Tk()는 윈도우를 자동으로 생성하는 클래스, 여기에 추가로 새로운 윈도우 또는 다이얼로그
#               만들경우 Toplevel을 사용
# Combobox
# Frame         컨테이너 위젯, 다른 위젯들을 그룹핑
# Canvas        그래프와 점들로 그림을 그릴 수 있는 위젯, 커스텀 위젯을 만들 때 사용
#
import tkinter as tk
# tkinter 패키지의 서브모듈 ttk를 가져옴
# ttk(themed tk를 의미): 개선된 GUI를 제공하기 위한 모듈
from tkinter import ttk

#윈도우 인스턴스 생성
win = tk.Tk()
win.title("====== Python GUI =======")
#win.resizable(False, False) # x, y

#ttk.Label(win, text="라벨").grid(column=0, row=0)
lb1 = ttk.Label(win, text="라벨")
lb1.grid(column=0, row=0)

btn1 = tk.Button(win, text="클릭")
btn1.grid(column=1, row=0)

# 기존에 사용하던 위젯 추가 방식
# lb1 = tk.Label(win, text="라벨")
# lb1.pack()

#GUI의 크기 변경 못하게

tk.mainloop() # 이벤트 순환문이 없으면 화면에 GUI가 보이질 않는다. # 이벤트가 전달되기를 기다리는 무한루프

#tkinter 패키지는 위젯이 없을 때는 기본 크기 사용
# 위젯 추가시, 일반적으로 위젯을 표시하는데 필요한 만큼의 공간만을 사용