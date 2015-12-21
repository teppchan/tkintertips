#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Tkinter as Tk
root=Tk.Tk()

for i in xrange(9):
    Tk.Button(root,
              text=("%d" % i),
    ).grid(row=2-i/3, column=i%3, sticky="news")

Tk.Button(root,
          text="0",
).grid(row=3, column=0, columnspan=2, sticky="news")

Tk.Button(root,
          text=".",
).grid(row=3, column=2, sticky="news")

Tk.Button(root,
          text="en\nter",
).grid(row=2, column=3, rowspan=2, sticky="news")

Tk.Button(root,
          text="+",
          bg="gray"
).grid(row=0, column=3, rowspan=2, sticky="news")

root.mainloop()
