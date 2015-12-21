#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

for c in ['flat', 'groove', 'raised', 'ridge', 'solid', 'sunken', ]:
    Tk.Label(root,
             text=c,
             width=10,
             borderwidth=4,
             relief=c).pack()

root.mainloop()


