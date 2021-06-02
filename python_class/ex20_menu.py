


import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("640x400")
win.resizable(True, True)
win.title("Menu Test")
win.configure(bg='yellow')

# Menu 만들기
#해당 윈도우 창에 메뉴를 사용할 수 있게 함
menu_bar = tk.Menu(win)

#해당 윈도우 창에 메뉴를 등록
win.config(menu = menu_bar)

def cmd_close():
    print("call cmd_close")
    win.quit()


#Menu Method
# add_command(인수): 기본 메뉴 항목 생성
# add_radiobutton(인수): 라디오 버튼 메뉴 항목 생성
# add_checkbutton(인수): 체크 버튼 메뉴 항목 생성
# add_cascade(인수): 상위 메뉴와 하위 메뉴를 연결
#   메뉴이름.add_cascade(label='하위메뉴이름', menu='연결할 하위 메뉴')
# add_separator(): 메뉴 구분선
# add(유형, 인수): 특정 유형의 메뉴항목 생성
# delete(start_index, end_index): start_index에서 end_index까지의 메뉴항목 삭제
# entryconfig(index, 인수): index위치의 메뉴 항목 수정
# index(item): item 메뉴항목의 index 위치를 반환
# insert_separator(index): index 위치에 구분선 생성
# invoke(index): index 위치의 항목 실행
# type(속성): 메뉴 유형을 반환(command, radiobutton, checkbutton, cascade, separator, tearoff)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="exit", command=cmd_close)
menu_bar.add_cascade(label="File", menu=file_menu)

radio_menu = tk.Menu(menu_bar, tearoff=0, selectcolor='blue', bg='yellow', relief='solid')
radio_menu.add_radiobutton(label="서브메뉴1")
radio_menu.add_radiobutton(label="서브메뉴2")
radio_menu.add_radiobutton(label="서브메뉴3")

menu_bar.add_cascade(label="Radio", menu=radio_menu)

check_menu = tk.Menu(menu_bar, tearoff=0, selectcolor='red', fg='red')
check_menu.add_checkbutton(label="Sub Menu1", state='disabled')
check_menu.add_checkbutton(label="Sub Menu2")
check_menu.add_checkbutton(label="Sub Menu3")

menu_bar.add_cascade(label="Check", menu=check_menu)


win.mainloop()