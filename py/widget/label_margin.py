#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

Tk.Label(root,
         text="Label",
         relief='groove'
).pack(padx=10, pady=40)
Tk.Label(root,
         text="Label",
         relief='groove'
).pack(padx=10, pady=30)

root.mainloop()
