from tkinter import Toplevel
from tkinter import Tk , BOTH
from tkinter.ttk import Frame , Button , Style , Label

class Window(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.master = master
        self.initUI()
        
        

    def initUI(self):

        self.master.title("Parent Window")
        self.pack(fill=BOTH , expand=1)
        self.button = Button(self,text="Create New Window", command=self.createWindow)
        self.button.pack(side="top")

        self.centerWindow()

    def centerWindow(self):

        w = 290
        h = 150

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw-w)/2
        y = (sh-h)/2

        self.master.geometry('%dx%d+%d+%d'%(w,h,x,y))

    def createWindow(self):

        self.parentWindowObject = Toplevel(self)
        self.parentWindowObject.wm_title("Window")

        self.label = Label(self.parentWindowObject,text="Hello")
        self.label.pack(side="top",fill=BOTH)

        self.button = Button(self.parentWindowObject,text="msg", command =self.msg)
        self.button.place(x=100,y=100)

        self.centerWindow()

    def msg(self):
        print ("Hello World!")

def main():
    root = Tk()
    
    window = Window(root)
    root.mainloop()

if __name__ == '__main__':
    main()
