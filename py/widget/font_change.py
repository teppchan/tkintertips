#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

Tk.Label(
    text='Font 1',
    font=('times', 20, ),
).pack()

Tk.Label(
    text='Font 2',
    font=('arial', 16, 'bold'),
).pack()

Tk.Label(
    text='Font 3',
    font=('gothic', 12, 'underline'),
).pack()

root.mainloop()
