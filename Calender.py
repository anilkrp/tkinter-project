from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import calendar

# Function here...
year=2020
text=calendar.calendar(year)
def next():
    global year
    year+=1
    print(year)
    l1.config(text=calendar.calendar(year))
    l0.config(text=f'Calendar {year}')
def preview():
    global year
    year-=1
    print(year)
    l1.config(text=calendar.calendar(year))
    l0.config(text=f'Calendar {year}')

root=Tk()
root.title('Title here ...')
root.resizable(False,False)
#code here...
l0=ttk.Label(root,text='Calender 2020',font=('Times 15 bold'))
l0.grid(row=0,column=1,padx=5,ipadx=5,ipady=5)
l1=ttk.Label(root,text=text,background='gray90',font=('Consolas',10,'bold'))
l1.grid(row=2,column=1,padx=10,pady=5)
ttk.Button(root,text='Next',command=next).grid(row=3,column=1,sticky='e',padx=5,pady=5)
ttk.Button(root,text='Preview',command=preview).grid(row=3,column=1,sticky='w',padx=5,pady=5)
root.config(background='lightgray')
root.mainloop()
