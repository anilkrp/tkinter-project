from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def play():
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
root=Tk()
root.title('Title here ...')
root.geometry('500x300')
root.resizable(False,False)
#code here...
l1=ttk.Label(root,text='',font=('times 200 bold'))
l1.pack()

ttk.Button(root,text='Play',command=play).place(x=210,y=270)


root.mainloop()
