#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

for i in xrange(9):
    Tk.Button(root,
              text=("grid %d" % i),
    ).grid(row=2-i/3, column=i%3)

root.mainloop()
