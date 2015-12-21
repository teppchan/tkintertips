#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

Tk.Label(root,
         text='hand',
         cursor='hand2',
         width=30,
).pack()

Tk.Label(root,
         text='watch',
         cursor='watch',
         width=30,
).pack()

root.mainloop()
