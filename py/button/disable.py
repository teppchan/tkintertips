#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

b=Tk.Button(root,
            text="Hello!!",
)
b.pack()

cb=Tk.BooleanVar()
def disable_b():
    if cb.get()==True:
        b['state']='disable'
    else:
        b['state']='normal'


c=Tk.Checkbutton(root,
                 text="disabled",
                 variable=cb,
                 command=disable_b
)
c.pack()

root.mainloop()

