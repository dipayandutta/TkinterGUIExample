from tkinter import *

class Window(Frame):

    def __init__(self,master=None):
        
        Frame.__init__(self,master)
        
        self.master     = master
        windowWidth     = root.winfo_reqwidth()
        windowHeight    = root.winfo_reqheight()

        print("Width ",windowWidth , "height" , windowHeight)

        positionRight   = int(root.winfo_screenwidth()/2 - windowWidth/2)
        positionHeight  = int(root.winfo_screenheight()/2 - windowHeight/2)

        root.geometry("+{}+{}".format(positionRight,positionHeight))
        master.minsize(width=300,height=300)
        
        Button(root,text='Press Me',command=self.msg).pack(side=LEFT)
        root.title("Cool window!!!")

    def msg(self):
        print("Hello World!")

root = Tk()
app  = Window(root)
root.mainloop()
