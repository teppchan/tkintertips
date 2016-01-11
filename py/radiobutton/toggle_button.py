#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

v=Tk.Variable()
v.set(1)

rb1=Tk.Radiobutton(
    text="RadioButton1",
    variable=v,
    value=1,
    indicatoron='off',
)
rb1.pack(fill='x')

rb2=Tk.Radiobutton(
    text="RadioButton2",
    variable=v,
    value=2,
)
rb2.pack(fill='x')

Tk.Label(
    textvariable=v,
).pack(fill='x')

root.mainloop()
