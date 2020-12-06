from tkinter import *
from tkinter import ttk
import time
import random
from tkinter import messagebox
def timeSet():
    global t
    t=0
    if ee.get()=='':
        messagebox.showerror('time error','Please enter number for timer set !')
    else:
        t=t+int(ee.get())
        b1.config(state=DISABLED)
        ee.config(state=DISABLED)
        b2.config(state=NORMAL)
        print('time set for :',t,'sec.')
def start():
    global t
    if t>0:
        l1.config(text=t,font=('Arial',35))
        print(t)
        t=t-1
        l1.after(1000,start)
    elif t==0:
        print('Time Up !')
        l1.config(text='Time Up !',font=('Arial',25))
        ee.config(state=NORMAL)
        b1.config(state=NORMAL)
        b2.config(state=DISABLED)

root=Tk()
root.title('Time Set')
root.resizable(False,False)
#code here...
l1=ttk.Label(root,text='Time Set',font=('arial',25,'bold'))
l1.grid(row=0,column=0,padx=25,pady=10)
times=StringVar()
ee=ttk.Entry(root,width=15,textvariable=times)
ee.grid(row=1,column=0,padx=25,pady=10)
b1=ttk.Button(root,text='Set',command=timeSet)
b2=ttk.Button(root,text='Click here',command=start,state=DISABLED)
b1.grid(row=2,column=0,padx=25,pady=2)
b2.grid(row=3,column=0,padx=25,pady=2)
root.mainloop()
