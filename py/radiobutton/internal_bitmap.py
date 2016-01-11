#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

bitmaps=["error", "gray12", "gray25", "gray50", "gray75",
         "hourglass", "info", "questhead", "question",
         "warning"]

v=Tk.Variable()
v.set(0)

for i,b in enumerate(bitmaps):
    cb=Tk.Radiobutton(root,
        text="Checkbutton",
        bitmap=b,
        value=i,
        variable=v,
        #indicatoron='off',
    )
    cb.pack(fill='x')

root.mainloop()
