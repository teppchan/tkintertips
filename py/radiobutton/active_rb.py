#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

v=Tk.Variable()
v.set(1)

rb1=Tk.Radiobutton(
    root,
    text="RadioButton1",
    variable=v,
    value=1,
)
rb1.pack(fill='x')

rb2=Tk.Radiobutton(
    root,
    text="RadioButton2",
    variable=v,
    value=2,
)
rb2.pack(fill='x')

Tk.Label(
    root,
    textvariable=v,
).pack(fill='x')

def select_rb1():
    rb1.select()
def deselect_rb1():
    rb1.deselect()

Tk.Button(
    root,
    text="RadioButton 1 select",
    command=select_rb1,
).pack(fill='x')

Tk.Button(
    root,
    text="RadioButton 1 deselect",
    command=deselect_rb1,
).pack(fill='x')

root.mainloop()
