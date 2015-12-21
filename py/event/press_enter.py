#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

f=Tk.Frame(root,
           width=200,
           height=100,
)
f.pack()

def print_return(event):
    print("Return!!")

root.bind("<Return>", print_return)

root.mainloop()
