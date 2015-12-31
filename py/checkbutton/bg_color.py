#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

cb=Tk.Checkbutton(root,
    text="Checkbutton",
    selectcolor='blue',
    indicatoron='off',
)
cb.pack(fill='x')

root.mainloop()
