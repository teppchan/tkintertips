#!/usr/bin/env python

import sys
import Tkinter as Tk
root=Tk.Tk()

Tk.Frame(root,
         width=200,
         height=100,
).pack()

root.bind("<Control-x><Control-c>", sys.exit)

root.mainloop()
