#!/usr/bin/env python
#-*- coding: utf-8 -*-
import Tkinter as Tk
root=Tk.Tk()

text=u"""つれづれなるまゝに、
日ぐらし硯に向かひて、
心にうつりゆくよしなしごとをそこはかとなく書き付くれば、
あやしうこそ物狂ほしけれ。
"""

m=Tk.Message(root,
             width=500,
             text=text,
)
m.pack()

root.mainloop()
