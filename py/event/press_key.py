#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

f=Tk.Frame(root,
           width=200,
           height=100,
)
f.pack()

def print_return(event):
    print("key pressed : %s\n" % event.keysym)

root.bind("<KeyPress>", print_return)

root.mainloop()
