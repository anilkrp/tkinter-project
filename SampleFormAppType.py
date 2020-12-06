from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class AppName:


    def __init__(self,master):

        self.master = master
        master.title('App title.....')
        master.resizable(False,False)


        #code write here...


def main():
    root=Tk()
    appname=AppName(root) # app name chnge here ...
    root.mainloop()
if __name__ == '__main__':main()
