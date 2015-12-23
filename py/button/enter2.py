#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

num=Tk.IntVar()
def inc_num(event=None):
    num.set(num.get()+1)

b=Tk.Button(root,
            text="Hello!!",
            command=inc_num
)
b.pack()

l=Tk.Label(root,
           textvariable=num,
)
l.pack()

def b_invoke(event=None):
    b.invoke()
root.bind("<Return>", b_invoke)

root.mainloop()

