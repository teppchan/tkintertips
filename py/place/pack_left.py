#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

Tk.Label(root, text="Left").pack(side='left')
Tk.Label(root, text="Center").pack(side='left')
Tk.Label(root, text="Right").pack(side='left')

root.mainloop()
