#!/usr/bin/env python

import Tkinter as Tk

root=Tk.Tk()
root.title(u"winfo")

def f_btn():
    print("width=%d height=%d" % (root.winfo_width(), root.winfo_height()))

btn=Tk.Button(root, text="window size", width=30)
btn.pack()
btn["command"]=f_btn

root.mainloop()
