import tkinter

root = tkinter.Tk()

def func(ev):
    label.config(text=e.get())

label = tkinter.Label(root, text="Input Text")
label.pack()

e = tkinter.Entry(root)
e.pack()

e.bind("<Return>", func)

root.mainloop()
