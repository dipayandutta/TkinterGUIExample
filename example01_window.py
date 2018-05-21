#! /usr/bin/python3

'''
    A Simple Window creation using python3 with tkinter
'''

from tkinter import Tk , BOTH , LEFT , Button
from tkinter.ttk import Frame

class Window(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.widget()

    def initUI(self):
        self.master.title("Example01_Window")
        self.pack(fill=BOTH,expand=1)

    def widget(self):
        Button(self,text="Click",command=self.msg).pack(side=LEFT)

    def msg(self):
        print ("Hello World!")
        
def main():

    root = Tk()
    root.geometry("250x150+300+300")
    app = Window()
    root.mainloop()

if __name__ == '__main__':
    main()
