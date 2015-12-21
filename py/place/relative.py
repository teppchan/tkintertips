#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()
root["width"]=300
root["height"]=200

Tk.Label(root,
         text="Label1",
         bg='green',
).place(relx=0.1, rely=0.8)

Tk.Label(root,
         text="Label2",
         bg='red',
).place(relx=0.8, rely=0.1)

root.mainloop()
