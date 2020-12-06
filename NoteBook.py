from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename

root=Tk()
root.title('Title here ...')
root.geometry('610x740')
#root.resizable(False,False)
#code here...
def openfile():
    filepath=askopenfilename(filetype=[('text files','*.txt'),('all file','*.*')])
    if not filepath:
        return
    book.delete('1.0',END)
    with open(filepath,'r') as loadfile:
        text=loadfile.read()
        book.insert(END,text)
        root.title(filepath)

def savefile():
    filepath=asksaveasfilename(filetype=[('text files','*.txt'),('all file','*.*'),('pdf file','*.pdf')])
    if not filepath:
        return
    with open(filepath,'w') as editfile:
        text=book.get('1.0',END)
        editfile.write(text)

def ClearAll():
    book.delete('1.0',END)

nbfrm=ttk.Frame(root)
nbfrm.pack()

l1=ttk.Label(nbfrm,text='NoteBook',font=('times 15 bold'))
l1.grid(row=0,column=1,columnspan=2)

b0=ttk.Button(nbfrm,text='Load File',command=openfile)
b1=ttk.Button(nbfrm,text='Save File',command=savefile)
b2=ttk.Button(nbfrm,text='Clear All',command=ClearAll)
b3=ttk.Button(nbfrm,text='Cancel',command=root.destroy)

b0.grid(row=2,column=0,sticky='w',pady=5)
b1.grid(row=2,column=1,sticky='e',pady=5)
b2.grid(row=2,column=2,sticky='w',pady=5)
b3.grid(row=2,column=3,sticky='e',pady=5)

book=Text(nbfrm,width=52,height=29,font=('arial 15'))
book.grid(row=1,column=0,columnspan=4)

root.mainloop()
