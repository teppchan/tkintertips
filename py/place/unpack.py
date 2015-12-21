#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

label=Tk.Label(root, text="Label")
label.pack(side='top')

def label_unpack():
    label.pack_forget()
button=Tk.Button(root, text="unpack", command=label_unpack)
button.pack(side='top')

root.mainloop()
