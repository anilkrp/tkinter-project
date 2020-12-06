from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def total():
    t1=e1.get()
    t2=e2.get()
    t3=e3.get()
    t4=e4.get()
    t5=e5.get()
    t=int(t1)*5+int(t2)*7+int(t3)*12+int(t4)*10+int(t5)+8
    print('total price :',t)
    l8.config(text=float(t))

root=Tk()
root.title('Title here ...')
root.geometry("700x500")
root.resizable(False,False)

#code here...
l1=ttk.Label(root,text='Menu',font=('times 28 bold'))
l1.place(x=500,y=10)
l2=ttk.Label(root,text='Tea  --  5 $',font=('times 15 bold'))
l2.place(x=460,y=60)
l3=ttk.Label(root,text='Coffee  --  7 $',font=('times 15 bold'))
l3.place(x=460,y=90)
l4=ttk.Label(root,text='Pizza  --  12 $',font=('times 15 bold'))
l4.place(x=460,y=120)
l5=ttk.Label(root,text='Burgger  --  10 $',font=('times 15 bold'))
l5.place(x=460,y=150)
l6=ttk.Label(root,text='Pateze  --  8 $',font=('times 15 bold'))
l6.place(x=460,y=180)
l7=ttk.Label(root,text='Total (in $) :',font=('times 18 bold'))
l8=ttk.Label(root,text='00.00',font=('times 18 bold'))
l7.place(x=150,y=340)
l8.place(x=150,y=370)


la1=ttk.Label(root,text='Tea')
la2=ttk.Label(root,text='Coffee')
la3=ttk.Label(root,text='Pizza')
la4=ttk.Label(root,text='Burgger')
la5=ttk.Label(root,text='Pateze')
la1.place(x=50,y=10)
la2.place(x=250,y=10)
la3.place(x=50,y=100)
la4.place(x=250,y=100)
la5.place(x=50,y=210)

e1=ttk.Entry(root,width=5)
e2=ttk.Entry(root,width=5)
e3=ttk.Entry(root,width=5)
e4=ttk.Entry(root,width=5)
e5=ttk.Entry(root,width=5)
e1.place(x=50,y=40)
e2.place(x=250,y=40)
e3.place(x=50,y=130)
e4.place(x=250,y=130)
e5.place(x=50,y=240)
ttk.Button(root,text='Total Price',command=total).place(x=150,y=300)


root.mainloop()
