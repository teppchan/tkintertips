#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()


for n in ["error", "gray12", "gray25", "gray50", "gray75",
          "hourglass", "info", "questhead", "question",
          "warning"
]:
    Tk.Button(root,
              bitmap=n,
              #fg="darkgreen",
    ).pack()

root.mainloop()
