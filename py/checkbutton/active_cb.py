#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

cb=Tk.Checkbutton(root,
        text="Checkbutton",
        )
cb.pack(fill='x')

def select():
    cb.select()
def deselect():
    cb.deselect()
def toggle():
    cb.toggle()

Tk.Button(root,
        text="select",
        command=select
        ).pack(fill='x')
Tk.Button(root,
        text="deselect",
        command=deselect,
        ).pack(fill='x')
Tk.Button(root,
        text="toggle",
        command=toggle,
        ).pack(fill='x')

root.mainloop()
