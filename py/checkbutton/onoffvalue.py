#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

v=Tk.StringVar()
v.set("checkOFF")

cb=Tk.Checkbutton(root,
    text="Checkbutton",
    variable=v,
    onvalue="checkON",
    offvalue="checkOFF",
)
cb.pack(fill='x')

Tk.Label(root,
    textvariable=v,
).pack(fill='x')

root.mainloop()
