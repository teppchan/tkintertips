#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

v=Tk.BooleanVar()
v.set(False)

l=Tk.Label(
    text="set False",
)
l.pack(fill='x')

def disp():
    print(v.get())
    if v.get()==False:
        l["text"]="set False"
    else:
        l["text"]="set True"

cb=Tk.Checkbutton(root,
    text="Checkbutton",
    variable=v,
    command=disp
)
cb.pack(fill='x')

root.mainloop()
