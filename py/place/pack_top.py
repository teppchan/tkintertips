#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

Tk.Label(root, text="Top").pack(side='top')
Tk.Label(root, text="Middle").pack(side='top')
Tk.Label(root, text="Bottom").pack(side='top')

root.mainloop()
