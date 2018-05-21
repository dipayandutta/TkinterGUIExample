#! /usr/bin/python3

"""
    Program to make the window in center of the screen 
"""

from tkinter import Tk, BOTH , Button
from tkinter.ttk import Frame

class Window(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

        
    def initUI(self):

        self.master.title("Example02_Center_Window")
        self.pack(fill=BOTH,expand=1)
        self.centerWindow()
        self.widget()

    def centerWindow(self):

        w = 290
        h = 150

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()


        x = (sw-w)/2
        y = (sh-h)/2

        self.master.geometry('%dx%d+%d+%d'%(w,h,x,y))

    def widget(self):

        clickme = Button(self,text="Click Me!",command=self.msg)
        clickme.place(x= 100,y=100)

    def msg(self):
        print ("Hello Wolrd!")

def main():
    root = Tk()
    window = Window()
    root.mainloop()

if __name__ == '__main__':
    main()

        
