#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

l=Tk.Label(root,
           text="Ruby",
)
l.pack()

def change_text():
    l["text"]="Python"

Tk.Button(root,
          text="Python",
          command=change_text,
).pack()

root.mainloop()
