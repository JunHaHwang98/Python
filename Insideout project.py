import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
import random
import os
import sys
import pandas as pd

window = Tk()
window.title("Insideout 추천인 코드")
window.geometry("300x240")

sexselect = ["남성", "여성", "알수없음 및 기타"]
bankselect= ["국민은행", "신한은행", "기업은행", "카카오뱅크", "하나은행", "우리은행", "토스뱅크", "새마을은행", "우체국은행", "케이뱅크", "저축은행", "KDB산업은행", "씨티은행", "SBI저축은행"]
sexselect1 = "U"

randomnum1 = str(random.randrange(0,10))
randomnum2 = str(random.randrange(0,10))
randomnum3 = str(random.randrange(0,10))
randomnum4 = str(random.randrange(0,10))
randomnum = (randomnum1+randomnum2+randomnum3+randomnum4)

def create():
    code2.config(text="완료")
    if sex1.get() == "남성":
        sexselect1 = "M"
    elif sex1.get() == "여성":
        sexselect1 = "W"
    elif sex1.get() == "알수없음 및 기타":
        sexselect1 = "E"
    else :
        str = StringVar()
        str = "성별이 선택되지 않았습니다."
        messagebox.showinfo("알림창" ,str)
    recode = (sexselect1+birth1.get()[2:6]+randomnum)
    code1.insert(0, recode)
    data = (name1.get(), sex1.get(), birth1.get(), payment1.get(), payment2.get(), contact1.get(), address1.get(), recode)
    excel1.insert(0, data)

def click(event):
    payment2.delete(0, "end")

def excel():
    pr = []
    pr.append[name1.get(), sex1.get(), birth1.get(), payment1.get(), payment2.get(), contact1.get(), address1.get(), recode]
    df = pd.DataFrame(pr, columns=['성명', '성별', '생년월일', '은행'. '계좌번호', '연락처', '주소', '추천인 코드'])
    writer = pd.ExcelWriter('Insideout.xlsx')
    df.to_excel(writer, 'Sheet1', index=False)

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)
    restart()

name = Label(window, text="성명")
name.grid(row=0, column=0)
name1 = Entry(window)
name1.grid(row=0, column=1)

sex = Label(window, text="성별")
sex.grid(row=1, column=0)
sex1 = ttk.Combobox(window, width=17, height=3, values=sexselect)
sex1.grid(row=1, column=1)
sex1.set("성별")

birth = Label(window, text="생년월일")
birth.grid(row=2, column=0)
birth1 = Entry(window)
birth1.grid(row=2, column=1)
secondcode = birth1.get()

payment = Label(window, text="결제 정보")
payment.grid(row=3, column=0)
payment1 = ttk.Combobox(window, width=17, height=5, values=bankselect)
payment1.grid(row=3, column=1)
payment1.set("은행 선택")
payment2 = Entry(window)
payment2.insert(0, "계좌번호 입력")
payment2.bind("<Button-1>", click)
payment2.grid(row=4, column=1)

contact = Label(window, text="연락처")
contact.grid(row=5, column=0)
contact1 = Entry(window)
contact1.grid(row=5, column=1)

address = Label(window, text="주소")
address.grid(row=6, column=0)
address1 = Entry(window)
address1.grid(row=6, column=1)

code = Label(window, text="추천인 코드")
code.grid(row=7, column=0)
code1 = Entry(window)
code1.grid(row=7, column=1)
code2 = Button(window, text="생성", command=create)
code2.grid(row=7, column=2)

excel = Label(window, text="데이터")
excel.grid(row=8, column=0)
excel1 = Entry(window)
excel1.grid(row=8, column=1)
excel2 = Button(window, text="추가", command=excel)
excel2.grid(row=8, column=2)

reset = Button(window, text="      재시작       ", command=restart)
reset.grid(row=9, column=1)

window.mainloop()
