import tkinter

root = tkinter.Tk()

def func():
    label.config(text="Pushed")

label = tkinter.Label(root, text="Push Button")
label.pack()

button = tkinter.Button(root, text="Push!", command = func)
button.pack()

root.mainloop()
