#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

l=Tk.Label(root,
           text="hoge",
)
l.pack()

def print_text():
    print("%s" % l["text"])

Tk.Button(root,
          text="print label text",
          command=print_text,
).pack()

root.mainloop()
