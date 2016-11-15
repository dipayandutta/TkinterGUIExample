'''Software Structure
Version =0.1
Coded By = Dipayan Dutta
coded On = 15th May 2016
'''

#importing Tkinter
from Tkinter import *
#importing matplotlib
import matplotlib.pyplot as plt


#creating class
class SoftwareStructure(Frame):

    def __init__(self,parent):#The constructor 
        Frame.__init__(self,parent)

        self.parent = parent
        self.FileMenu(parent)
        self.Fields(parent)
        self.plotGraph(parent)

    def FileMenu(self,parent):#Creating file menu

        self.parent.title("Software Structure at StartUP!")

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        #creating the fileMenu
        fileMenu = Menu(menubar,tearoff=0)
        fileMenu.add_command(label="click",command = self.printClick)
        #This below line add_cascade is important because it add the menu on the screen
        menubar.add_cascade(label="click",menu=fileMenu)
        #creating the edit Menu
        editMenu = Menu(menubar,tearoff=0)
        editMenu.add_command(label="Edit",command=self.printEdit)
        menubar.add_cascade(label="Click to See Edit",menu=editMenu)


    def Fields(self,parent):

        self.parent = parent
        #creating First Label
        self.userNameLabel = Label(parent,text="username")
        self.userNameLabel.pack(fill=X)
        #creating First Entry
        self.usernameEntry = Entry(parent,bd=5,width=10)
        self.usernameEntry.pack(fill=X)

        #creating password Label
        self.passwordLabel = Label(parent,text="password")
        self.passwordLabel.pack(fill=X)
        #creating password Entry
        self.passwordEntry = Entry(parent,bd=5,width=10,show="*")
        self.passwordEntry.pack(fill=X)

        #creating submit Button
        self.submitButton = Button(parent,text="Login",command=self.check)
        self.submitButton.pack()

    def plotGraph(self,parent):

        #creating One x1label for plot data's
        self.x1Label =Label(parent,text="Enter X1")
        self.x1Label.pack(fill=X)

        #creating Entry for getting plot values
        self.x1LabelEntry = Entry(parent,bd=5,width=10)
        self.x1LabelEntry.pack(fill=X)

        #creating One x2label for plot data's
        self.x2Label =Label(parent,text="Enter X2")
        self.x2Label.pack(fill=X)

        #creating Entry for getting plot values
        self.x2LabelEntry = Entry(parent,bd=5,width=10)
        self.x2LabelEntry.pack(fill=X)

        #creating button to get the numerics
        self.getNumerics = Button(parent,text="Plot!",command=self.plot)
        self.getNumerics.pack()

    def plot(self):
        array=[]
        print self.x1LabelEntry.get()
        print self.x2LabelEntry.get()
        array.append(self.x1LabelEntry.get())
        array.append(self.x2LabelEntry.get())
        
        print len(array)
        print array

        plt.plot(array)
        plt.ylabel('some numbers')
        plt.show()
        
    def printClick(self):
        print "Click"

    def printEdit(self):
        print "Edit "

    def check(self):
        print "Getting Username and password From the Field!"
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        print username
        print password

        if username == "james" and password == "bond":
            print "opening portal!"
            anotherDimension()
        else:
            print "Please check to open portal!"

    


def main ():
    root = Tk()
    root.geometry("250x350+300+300")
    application = SoftwareStructure(root)
    root.mainloop()

if __name__ == '__main__':
    main()
