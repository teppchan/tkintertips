#!/usr/bin/env python

import Tkinter as Tk

root=Tk.Tk()
root.title(u"Hello Tk window!")
root["width"]=300
root["height"]=200

def f_btn():
    print("width=%d height=%d" % (root["width"], root["height"]))
btn=Tk.Button(root, text="window size", width=30)
btn.pack()
btn["command"]=f_btn

root.mainloop()
