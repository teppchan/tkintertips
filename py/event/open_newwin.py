#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

l=Tk.Label(root,
           text="Push F1"
)
l.pack()

def top_win(event):
    Tk.Toplevel(root)

root.bind("<F1>", top_win)

root.mainloop()
