# Scrollbar 위젯
# 생성: Scrollbar(윈도우창, 인수...) 인수(파라미터)를 이용하여 스크롤바의 속성을 설정

import tkinter as tk

win = tk.Tk()
win.title("Listbox Test")
win.geometry("600x400")
win.resizable(False, False)

# 리스트 박스 생성
lbox = tk.Listbox(win)
#lbox.grid(row=0, column=0)
lbox.insert(0, "파이썬")
lbox.insert(1, "자바")
lbox.insert(2, "C#")
lbox.pack(padx=20, pady=20)

def selList():
    #현재 선택된 Index를 리턴해주는 메소드 curselection()
    # item = lbox.curselection()
    # print(item)
    # print(lbox.get(item))
    # print(lbox.size())
    for i in range(lbox.size()):
        print("{} : {}".format(i, lbox.get(i)))

    print(lbox.get(0, lbox.size()))

btn = tk.Button(win, text="확인", command=selList)
btn.pack()

# Listbox method
#   insert(index, '항목명'): index 위치에 목록을 추가
#   delete(start_index, end_index): start_index 부터 end_index 까지 목록 삭제
#   size(): 목록 개수를 리턴
#   activate(index) : index의 항목을 선택
#   curselection() : 선택된 목록의 index를 튜플로 반환
#   get(start_index, end_index) : 처음부터 끝까지 항목을 튜플 형태로 갖고옴
#   xview(): 가로 스크롤을 연결
#   yview(): 세로 스크롤을 연결

win.mainloop()
