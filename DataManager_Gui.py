import tkinter as tk
import tkinter.messagebox as mb
import pickle
import pyrebaseconfig


mainwin = tk.Tk()
menubar = tk.Menu(mainwin)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=mainwin.destroy)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Create new Configuration file", command = pyrebaseconfig.createconfig)
editmenu.add_command(label="Show Configuration file", command = pyrebaseconfig.Loadconfig)
menubar.add_cascade(label="Edit", menu=editmenu)

mainwin.config(menu = menubar)
mainwin.mainloop()
