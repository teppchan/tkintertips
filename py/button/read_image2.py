#!/usr/bin/env python

import PIL.ImageTk as ImageTk
import Tkinter as Tk
root=Tk.Tk()

imagetk=ImageTk.PhotoImage(file="py/button/cat.jpg")
Tk.Button(root,
          image=imagetk
).pack()

root.mainloop()
