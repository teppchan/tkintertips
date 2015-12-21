#!/usr/bin/env python

import Tkinter as Tk

root=Tk.Tk()
label=Tk.Label(root, text="Hello!", width=30)
label.pack()

def f_btn1():
    label["width"]+=10
    print("%d" % label["width"])
def f_btn2():
    label["width"]-=10
    print("%d" % label["width"])

btn1=Tk.Button(root, text=u"Wide", command=f_btn1)
btn1.pack()

btn2=Tk.Button(root, text=u"Narrow", command=f_btn2)
btn2.pack()

root.mainloop()
