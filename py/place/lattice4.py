#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

Tk.Button(root,
          text="ABC",
).grid(row=0, column=0, sticky="news")

Tk.Button(root,
          text="ABC\nabc",
).grid(row=0, column=1, sticky="news")

Tk.Button(root,
          text="ABCABC\nABCABC",
).grid(row=1, column=0, sticky="news")

Tk.Button(root,
          text="ABCABC",
).grid(row=1, column=1, sticky="news")

Tk.Grid.columnconfigure(root, 0, weight=1)
Tk.Grid.columnconfigure(root, 1, weight=1)
Tk.Grid.rowconfigure(root, 0, weight=1)
Tk.Grid.rowconfigure(root, 1, weight=1)

root.mainloop()
