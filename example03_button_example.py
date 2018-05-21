#! /usr/bin/python3

"""
    Program to make a quit Button 
"""

from tkinter import Tk , BOTH
from tkinter.ttk import Frame , Button , Style

class Window(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.style = Style()
        self.style.theme_use("default")
        self.master.title("Quit Button Example")
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

        quitButton = Button(self,text="quit",command=self.quit)
        quitButton.place(x=50,y=50)

def main():
    root = Tk()
    window = Window()
    root.mainloop()

if __name__ == '__main__':
    main()

        
