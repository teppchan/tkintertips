#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()
root["width"]=300
root["height"]=200

Tk.Label(root,
         text="Label",
         bg='green',
).place(x=50, y=100)

Tk.Label(root,
         text="Label",
         bg='red',
).place(x=200, y=30)

root.mainloop()
