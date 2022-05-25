import tkinter.ttk as ttk
from tkinter import *

window = Tk()
window.title("Insideout 추천인 코드")
window.geometry("320x240")

sexselect = ["남성", "여성", "알수없음 및 기타"]
bankselect= ["국민은행", "신한은행", "기업은행", "카카오뱅크", "하나은행", "우리은행", "토스뱅크", "새마을은행", "우체국은행", "케이뱅크", "저축은행", "KDB산업은행", "씨티은행", "SBI저축은행"]

def create():
    code.config(text="     생성 완료     ")

def click(event):
    payment2.delete(0, "end")

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

code = Button(window, text="추천인 코드 생성", command=create)
code.grid(row=7, column=0)
code1 = Label(window, text="M07061234")
code1.grid(row=7, column=1)

window.mainloop()
