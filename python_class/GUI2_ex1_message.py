# Message 위젯
# Message Parameter
# text, textvariable, anchor, justify
# width, height, relief, borderwidth(bd), bg, fg, padx, pady
# aspect : 메시지 높이에 대한 너비 비율 (default : 150)
# font : 메시지 문자열의 글꼴
# takefocus : Tab을 이용하여 포커스 이동 허용 여부 (default : True)
import tkinter

window=tkinter.Tk()
window.title("Message Test")
window.geometry("640x400+100+100")
window.resizable(False, False)

message=tkinter.Message(window, text="메세지 테스트입니다.", width=200, relief="solid")
message.pack()

window.mainloop()