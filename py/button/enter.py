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
b.bind("<Return>", inc_num)
b.pack()
b.focus()

l=Tk.Label(root,
           textvariable=num,
)
l.pack()

root.mainloop()

