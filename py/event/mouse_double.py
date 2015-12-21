#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

l=Tk.Label(root,
         width=10,
         height=2,
         text="Hello!!",
)
def print_click(event):
    print("Double-clicked\n")
l.bind("<Double-1>", print_click)
l.pack()

root.mainloop()
