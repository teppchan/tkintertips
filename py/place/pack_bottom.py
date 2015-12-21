#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

Tk.Label(root, text="Bottom").pack(side='bottom')
Tk.Label(root, text="Middle").pack(side='bottom')
Tk.Label(root, text="Top").pack(side='bottom')

root.mainloop()
