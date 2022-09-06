
from ctypes import resize
import tkinter as tk
import os
import json

from PIL import ImageTk,Image
global filePath
filePath='C:\\Users\\hongik\\Desktop\\[원천]babel_09\\Day15_201015_F\\1\\A\\313-2-1-15-Z51_A'
global idx

global files

global val1
global val2
global val3
global val4
global label
val1=False
val2=False
val3=False
val4=False
global image


if os.path.exists(filePath):
    files=os.listdir(filePath)


root=tk.Tk()



root.geometry("1080x980")
root.resizable(True, True)
#C:\Users\hongik\Desktop\[원천]babel_09\Day15_201015_F\1\A\313-2-1-15-Z51_A
label1=tk.Label(root,text='형식 : C:\\Users\\hongik\\Desktop\\[원천]babel_09\\Day15_201015_F\\1\\A\\313-2-1-15-Z51_A')
label1.pack()

def func(ev):
    global image
    global files
    global idx
    global filePath
    idx=0
    filePath=e.get()
    if os.path.exists(filePath):
        files=os.listdir(filePath)
    image=Image.open(filePath+'\\'+files[idx])
    image=image.crop((700,250,1400,800))
    image=ImageTk.PhotoImage(image,)
    label.config(image=image)


e=tk.Entry(root)
e.pack()
e.bind('<Return>', func)

image=None
label=tk.Label(root, image=image,)
label.pack()
def prev_command():
    global image
    global files
    global idx
    global filePath
    if idx>0:
        idx-=1
        image=Image.open(filePath+'\\'+files[idx])
        image=image.crop((700,250,1400,800))
        image=ImageTk.PhotoImage(image,)
        label.config(image=image)
            

prev_btn=tk.Button(root,text='prev',command=prev_command)

prev_btn.pack()

def com():
    global idx
    global files
    global image
    temp={"name":files[idx],"data":[val1,val2,val3,val4]}
    with open(filePath+'\\'+files[idx][:-4]+".json",'w',encoding="utf-8") as make_file:
        json.dump(temp,make_file)
    idx+=1
    image=Image.open(filePath+'\\'+files[idx])
    image=image.crop((700,250,1400,800))
    image=ImageTk.PhotoImage(image,)
    label.config(image=image)
    


CheckVariety_1=tk.IntVar()
CheckVariety_2=tk.IntVar()
CheckVariety_3=tk.IntVar()
CheckVariety_4=tk.IntVar()

def checkCom1():
    global val1
    if val1 :
        val1=False
    else:
        val1=True
    print(val1)

def checkCom2():
    global val2
    if val2 :
        val2=False
    else:
        val2=True
    print(val2)
def checkCom3():
    global val3
    if val3 :
        val3=False
    else:
        val3=True
    print(val3)
def checkCom4():
    global val4
    if val4 :
        val4=False
    else:
        val4=True
    print(val4)
check1=tk.Checkbutton(root,text='척추 중립',variable=CheckVariety_1,command=checkCom1)
check2=tk.Checkbutton(root,text='고개 정면',variable=CheckVariety_2,command=checkCom2)
check3=tk.Checkbutton(root,text='무릎 방향',variable=CheckVariety_3,command=checkCom3)
check4=tk.Checkbutton(root,text='발바닥 고정',variable=CheckVariety_4,command=checkCom4)
check1.pack(side = "left")
check2.pack(side = "left")
check3.pack(side = "left")
check4.pack(side = "left")
save=tk.Button(root,text='save and next',command=com)
def keyEvent(event):
    global idx
    global files
    global image
    temp={"name":files[idx],"data":[val1,val2,val3,val4]}
    with open(filePath+'\\'+files[idx][:-4]+".json",'w',encoding="utf-8") as make_file:
        json.dump(temp,make_file)
    if idx ==len(files)-1:
        print("마지막 사진입니다")
    else:
        idx+=1
        image=Image.open(filePath+'\\'+files[idx])
        image=image.crop((700,250,1400,800))
        image=ImageTk.PhotoImage(image,)
        label.config(image=image)
root.bind('<space>',keyEvent)
save.pack(side = "left")
root.mainloop()
