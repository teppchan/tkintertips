#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

f=Tk.Frame(root,
           width=200,
           height=100,
)
def print_motion(event):
    print("Motion!!")

f.bind("<Motion>", print_motion)
f.pack()

root.mainloop()
