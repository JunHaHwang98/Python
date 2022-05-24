import tkinter.ttk as ttk
from tkinter import *

window = Tk()
window.title("Insideout 추천인 코드")
window.geometry("320x240")

sexselect = ["남성", "여성", "알수없음 및 기타"]

def create():
    code.config(text="     생성 완료     ")

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

payment = Label(window, text="결제 정보")
payment.grid(row=3, column=0)

contact = Label(window, text="연락처")
contact.grid(row=4, column=0)
contact1 = Entry(window)
contact1.grid(row=4, column=1)

address = Label(window, text="주소")
address.grid(row=5, column=0)

code = Button(window, text="추천인 코드 생성", command=create)
code.grid(row=6, column=0)
code1 = Label(window, text="M07061234")
code1.grid(row=6, column=1)

window.mainloop()
