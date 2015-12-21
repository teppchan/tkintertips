#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

Tk.Button(root,
          text="wide wide wide wide wide"
).pack(fill='x')

Tk.Button(root,
          text="narrow"
).pack(fill='x')

root.mainloop()
