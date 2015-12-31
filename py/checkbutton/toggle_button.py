#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

v=Tk.Variable()
v.set(False)

cb=Tk.Checkbutton(root,
    text="checkbutton",
    variable=v,
    indicatoron='off',
    )
cb.pack(fill='x')

root.mainloop()
