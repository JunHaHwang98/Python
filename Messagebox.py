from tkinter import *
from tkinter import messagebox

root = Tk()

def button_click():
    str = "아무것도 선택되지 않았습니다."
    if Radiovar.get() == 1:
        str = "남자가 선택되었습니다."
    if Radiovar.get() == 2:
        str = "여자가 선택되었습니다."
    messagebox.showinfo("알림창", str)

str = StringVar()

Radiovar = IntVar()

Radio_button1 = Radiobutton(text="남자", variable=Radiovar, value=1)
Radio_button2 = Radiobutton(text="여자", variable=Radiovar, value=2)
Click_button = Button(text="선택", command=button_click)

Radio_button1.pack()
Radio_button2.pack()
Click_button.pack()

root.mainloop()
