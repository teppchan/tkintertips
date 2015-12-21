#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

Tk.Button(root,
          text="Button1"
).pack()

Tk.Button(root,
          text="Button2"
).pack(fill='x', expand=True)

Tk.Button(root,
          text="Button3"
).pack(fill='both', expand=True)


root.mainloop()
