#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

for s in [10, 12, 14, 16, 20]:
    Tk.Label(
        text=('Font size=%d' % s),
        font=('times', s ),
    ).pack()

root.mainloop()
