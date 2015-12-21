#!/usr/bin/env python

import Tkinter as Tk
root=Tk.Tk()

l=Tk.Label(root,
           text='red',
           bg='green',
           width=40,
)
def label_enter(event):
    l['bg']='red'
def label_leave(event):
    l['bg']='green'

l.bind('<Enter>', label_enter)
l.bind('<Leave>', label_leave)
l.pack(fill='x')

b=Tk.Button(root,
            text='red',
            activebackground='red',
            width=40,
).pack(fill='x')

root.mainloop()
