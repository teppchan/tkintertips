#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

image1=Tk.PhotoImage(file="bipolarc.gif")
Tk.Button(root,
          image=image1
).pack()

root.mainloop()
