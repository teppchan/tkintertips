#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

Tk.Label(root, text="Right").pack(side='right')
Tk.Label(root, text="Center").pack(side='right')
Tk.Label(root, text="Left").pack(side='right')

root.mainloop()
