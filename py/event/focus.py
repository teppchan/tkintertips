#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

def change_red(event):
    event.widget["fg"]="red"
def change_green(event):
    event.widget["fg"]="green"

for i in xrange(3):
    buf=Tk.StringVar()
    buf.set("Entry %d" % i)
    e=Tk.Entry(root,
               textvariable=buf
    )
    e.bind("<FocusIn>", change_red)
    e.bind("<FocusOut>", change_green)
    e.pack(side="top", fill="x")

root.mainloop()
