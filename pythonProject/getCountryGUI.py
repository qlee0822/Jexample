# -*- coding: utf-8 -*-
import os
import geoip2.database
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import re
from tkinter import *
from tkinter import filedialog
from datetime import datetime
from ipwhois import IPWhois
import pprint
import clipboard

os.chdir(os.path.dirname(os.path.abspath(__file__)))

root = Tk()
root.title("국가정보 확인 version 0.5")
root.geometry("1024x600")


def open_file():
    response = 1
    if lbl_dest_path.cget("text") != "":
        response = msgbox.askokcancel("알림", "기존 자료가 있습니다. 진행하시면 기존 자료는 삭제됩니다")

    if response == 0:
        return
    else:
        lbl_dest_path.config(text="")
        treeview.delete(*treeview.get_children())

    ips = []
    countries = []
    ip_text_file_fullpath = filedialog.askopenfilename( \
        initialdir=os.path.dirname(os.path.abspath(__file__)), \
        title="아이피 리스트 파일을 선택하세요", \
        filetypes=(("txt files", "*.txt"), ("all files", "*.*")) \
        )

    if ip_text_file_fullpath == "":
        pass
    else:
        lbl_dest_path.config(text=ip_text_file_fullpath)
        ip_list_file = open(ip_text_file_fullpath, "r")
        for text in ip_list_file.readlines():
            text = text.rstrip()
            ips.append(text)
        ip_list_file.close()

    if len(ips) > 0:
        for ipaddr in ips:
            country = ""
            try:
                country = reader.country(ipaddr).country.name
            except Exception as err:
                country = str(err)
            finally:
                countries.append(country)

        for i in range(0, len(ips)):
            if i % 2 == 0:
                treeview.insert('', 'end', text=i + 1, values=(ips[i], countries[i]), tags=('even',))
            else:
                treeview.insert('', 'end', text=i + 1, values=(ips[i], countries[i]), tags=('odd',))


# 전체 삭제
def delete_all():
    lbl_dest_path.config(text="")
    treeview.delete(*treeview.get_children())


def directdb_search_ip():
    ipaddr = txt_direct_ip.get()

    if ipaddr != "":
        country = ""
        try:
            if ip_regexpress(ipaddr) == 0:
                msgbox.showwarning("오류", "지원하지 않는 IP형식입니다.")
                txt_direct_ip.delete(0, END)
                txt_direct_result.delete("1.0", END)
                return
            country = reader.country(ipaddr).country.name
        except Exception as err:
            country = str(err)
        finally:
            result = ipaddr + '\t' + country
            txt_direct_result.delete("1.0", END)
            txt_direct_result.insert(END, result)
    else:
        return


def directweb_search_ip():
    ipaddr = txt_direct_ip.get()
    result_txt = ""
    if ipaddr != "":
        try:
            if ip_regexpress(ipaddr) == 0:
                msgbox.showwarning("오류", "지원하지 않는 IP형식입니다.")
                txt_direct_ip.delete(0, END)
                txt_direct_result.delete("1.0", END)
                return
            obj = IPWhois(ipaddr)
            results = obj.lookup_whois(get_referral=True)

            nets = None
            if 'nir' in results:
                nets = results['nir']['nets'][0]
            else:
                nets = results['nets'][0]

            result_txt = "query : " + str(results['query'])

            for key in nets:
                result_txt += "\n{0} : {1}".format(key, nets[key])

            result_txt += "\n\n" + "================== 전체내용 ==================" + "\n\n"
            result_txt += pprint.pformat(results)

        except Exception as err:
            result_txt += str(err)
        finally:
            pass
            txt_direct_result.delete("1.0", END)
            txt_direct_result.insert(END, result_txt)
    else:
        return


# 아이피 양식 체크
def ip_regexpress(input_ip):
    input_ip = input_ip.rstrip()
    regex = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})$', input_ip)
    return len(regex)


# 선택된 표 데이터를 텍스트 형태로 변환
def copy_treedata(seleted_data):
    result_txt = ""
    if len(seleted_data) > 0:
        for key in seleted_data:
            lst_value = treeview.item(key)["values"]
            result = lst_value[0] + '\t' + lst_value[1] + '\n'
            result_txt += result
        result_txt = result_txt[0:-1]
        clipboard.copy(result_txt)
        return result_txt
    else:
        return


# 선택영역 복사
def select_copy():
    if len(treeview.selection()) == 0:
        msgbox.showwarning("오류", "선택된 데이터가 없습니다.")
        return
    clipboard.copy(copy_treedata(treeview.selection()))


# 전체 복사
def all_copy():
    if len(treeview.get_children()) == 0:
        msgbox.showwarning("오류", "IP리스트 결과가 없습니다.")
        return
    clipboard.copy(copy_treedata(treeview.get_children()))


# 텍스트를 파일로 저장
def save_data(save_txt):
    if len(save_txt) == 0:
        msgbox.showwarning("오류", "저장할 데이터가 없습니다.")
        return
    else:
        save_text_file_fullpath = filedialog.asksaveasfilename( \
            initialdir=os.path.dirname(os.path.abspath(__file__)), \
            title="저장할 파일을 선택하세요", \
            filetypes=(("txt files", "*.txt"), ("all files", "*.*")) \
            )
        file_w = open(save_text_file_fullpath, "w")
        try:
            file_w.write(save_txt)
        except Exception as err:
            print(err)
        finally:
            file_w.close()


# 선택영역 저장
def select_save():
    if len(treeview.selection()) == 0:
        msgbox.showwarning("오류", "선택된 데이터가 없습니다.")
        return
    else:
        save_data(copy_treedata(treeview.selection()))


# 전체 저장
def all_save():
    if len(treeview.get_children()) == 0:
        msgbox.showwarning("오류", "IP리스트 결과가 없습니다.")
        return
    else:
        save_data(copy_treedata(treeview.get_children()))


mdb_frame = LabelFrame(root, text="GeoLite2-Country.mmdb 정보")
lbl_mmdb = Label(mdb_frame, text="GeoLite2-Country.mmdb정보가 없습니다.")
lbl_mmdb.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

try:
    reader = geoip2.database.Reader('GeoLite2-Country.mmdb')
    strtime = str(datetime.fromtimestamp(reader.metadata().build_epoch))
    lbl_mmdb.config(text="Last Update: " + strtime)
except:
    lbl_mmdb.config(text="Not find MMDB file : GeoLite2-Country.mmdb")

iplist_frame = LabelFrame(root, text="IP리스트")

# IP리스트 열기
btn_open_file = Button(iplist_frame, width=10, text="열기", command=open_file)
btn_open_file.pack(side="left", padx=5, pady=5)

# txt_dest_path = Entry(iplist_frame)
lbl_dest_path = Label(iplist_frame)
lbl_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)  # 높이 변경

# 전체삭제 버튼
btn_delete_all = Button(iplist_frame, width=10, text="전체삭제", command=delete_all)
btn_delete_all.pack(side="right", padx=5, pady=5)

# 직접입력 프레임
direct_frame = LabelFrame(root, text="직접입력")
lbl_direct_ip = Label(direct_frame, text="IP: ").grid(column=0, row=0, padx=5, pady=5)
txt_direct_ip = Entry(direct_frame, width=50)
txt_direct_ip.grid(column=1, row=0, columnspan=2, padx=5, pady=5, ipady=4)
lbl_direct_search_ip = Label(direct_frame, text="검색: ").grid(column=0, row=1, padx=3, pady=3)

# DB검색 버튼
btn_directdb_search_ip = Button(direct_frame, width=10, text="DB검색", command=directdb_search_ip)
btn_directdb_search_ip.grid(column=1, row=1, padx=5, pady=5, sticky=N + E + W + S)

# WEB검색 버튼
btn_directweb_search_ip = Button(direct_frame, width=10, text="WEB검색", command=directweb_search_ip)
btn_directweb_search_ip.grid(column=2, row=1, padx=5, pady=5, sticky=N + E + W + S)

# 직접입력 결과 프레임
direct_result_frame = LabelFrame(root, text="직접입력 결과", height=340, width=420)
txt_direct_result = Text(direct_result_frame, width=410, state="normal")
txt_direct_result.pack(fill="both", padx=5, pady=5, expand=True)

result_scrollbar = Scrollbar(txt_direct_result)
result_scrollbar.pack(side=RIGHT, fill="y")
result_scrollbar.config(command=txt_direct_result.yview)
txt_direct_result.config(yscrollcommand=result_scrollbar.set)

# IP입력 결과 프레임

ip_result_frame = LabelFrame(root, text="IP리스트 결과")
style = ttk.Style(ip_result_frame)
style.theme_use('classic')
style.map("mystyle.treeview", background=[('selected', '#BF00BF')])
style.layout("mystyle.treeview", [('mystyle.treeview.treearea', {'sticky': 'nswe'})])
treeview = ttk.Treeview(ip_result_frame, style="mystyle.treeview")
treeview["columns"] = ("one", "two")

treeview.tag_configure('odd', background='#FFFFFF')
treeview.tag_configure('even', background='#EFEFEF')

treeview.column("#0", width=40, stretch=NO)
treeview.heading("#0", text="순", anchor="center")

treeview.column("#1", width=120, stretch=NO)
treeview.heading("#1", text="IP", anchor="center")

treeview.column("#2", width=380, stretch=NO)
treeview.heading("#2", text="Country", anchor="center")

treeview_scrollbar = Scrollbar(ip_result_frame, orient="vertical", command=treeview.yview)
treeview_scrollbar.pack(side=RIGHT, fill="y")
treeview.config(yscrollcommand=treeview_scrollbar.set)

treeview.pack(side="left", fill="y", padx=5, pady=5, expand=True)

# 명령어 버튼 프레임
btn_command_frame = LabelFrame(root)

# 선택영역 복사 버튼
btn_select_copy = Button(btn_command_frame, width=13, text="선택영역복사", command=select_copy)
btn_select_copy.grid(column=0, row=0, padx=5, pady=5, sticky=N + E + W + S)

# 전체복사 버튼
btn_all_copy = Button(btn_command_frame, width=13, text="전체복사", command=all_copy)
btn_all_copy.grid(column=1, row=0, padx=5, pady=5, sticky=N + E + W + S)

# 선택영역 저장 버튼
btn_select_save = Button(btn_command_frame, width=13, text="선택영역저장", command=select_save)
btn_select_save.grid(column=2, row=0, padx=5, pady=5, sticky=N + E + W + S)

# 전체저장 버튼
btn_all_save = Button(btn_command_frame, width=13, text="전체저장", command=all_save)
btn_all_save.grid(column=3, row=0, padx=5, pady=5, sticky=N + E + W + S)

# 닫기 버튼
btn_close = Button(btn_command_frame, width=13, text="닫기", command=root.quit)
btn_close.grid(column=4, row=0, padx=5, pady=5, sticky=N + E + W + S)

# 위젯배치 place
mdb_frame.place(x=10, y=10, width=420)
iplist_frame.place(x=10, y=80, width=420)
ip_result_frame.place(x=440, y=10, height=530)
direct_frame.place(x=10, y=150, width=420)
direct_result_frame.place(x=10, y=250, width=420, height=340)
btn_command_frame.place(x=440, y=550, width=575, height=40)

root.resizable(False, False)
root.mainloop()