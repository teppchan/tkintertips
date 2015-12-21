#!/usr/bin/env python

import Tkinter as Tk

root=Tk.Tk()
Tk.Label(root,
         width=30,
         text='Green',
         fg='green',
         bg='red').pack()

root.mainloop()
