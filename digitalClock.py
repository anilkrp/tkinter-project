from tkinter import *
from tkinter import ttk
import sys
import time
def times():
    current_time=time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)

root=Tk()
#code here...
root.geometry('335x230')
root.resizable(False,False)
clock=Label(root,font=('times',50,'bold'),bg='white')
clock.grid(row=2,column=0,columnspan=3,pady=10,padx=25,ipadx=5,ipady=5)
times()
ttk.Label(root,text='Digital Timer',font=('times',40,'bold')).grid(row=0,column=0,columnspan=3,padx=10)
ttk.Label(root,text='Hour',font=('times',20,'bold')).grid(row=3,column=0)
ttk.Label(root,text='Minute',font=('times',20,'bold')).grid(row=3,column=1)
ttk.Label(root,text='Second',font=('times',20,'bold')).grid(row=3,column=2)

root.mainloop()
