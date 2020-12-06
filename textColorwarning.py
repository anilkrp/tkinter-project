from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

# Function here...
def warn():
    list1=['red','green','orange','blue','white','pink','gray']
    l1.config(background=random.choice(list1))
    l1.after(150, warn)

root=Tk()
root.title('WARNING...')
root.resizable(False,False)
# Code here...
l1=ttk.Label(root,text='This is Warning !!!',font=('arial',30,'bold'))
l1.pack()
warn()
root.mainloop()
