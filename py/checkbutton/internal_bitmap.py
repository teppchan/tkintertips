#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

for n in ["error", "gray12", "gray25", "gray50", "gray75",
          "hourglass", "info", "questhead", "question",
          "warning"
]:
    cb=Tk.Checkbutton(root,
        text="Checkbutton",
        bitmap=n,
        #indicatoron='off',
    )
    cb.pack(fill='x')

root.mainloop()
