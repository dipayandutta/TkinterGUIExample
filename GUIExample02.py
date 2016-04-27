import Tkinter
import tkMessageBox

class GuiExampleCode :
    def __init__(self,master):
        self.master = master

        self.L1 = Tkinter.Label(master,text="username")
        self.L1.pack()

        self.E1 = Tkinter.Entry(master,bd =5,width=10)
        self.E1.pack()

        self.L2 = Tkinter.Label(master,text="password")
        self.L2.pack()

        self.E2 = Tkinter.Entry(master,bd=5)
        self.E2.pack()

        self.submitButton = Tkinter.Button(master,text="Login",command=self.check)
        self.submitButton.pack()

    def check(self):
        print "Checking Username and password is in progress!!!"
        username = self.E1.get()
        password = self.E2.get()

        print "username is == "+str(username)
        print "password is == "+str(password)

        if (username == "" and password == ""):
            tkMessageBox.showinfo("Please enter username and password!")
        if (username == "james" and password == "bond"):
            self.openPage()
        #print (self.E1.get())
        #print (self.E2.get())
    def openPage(self):
        print "New Page is to open"
        top = Tkinter.Tk()
        top.mainloop()
        

root = Tkinter.Tk()
gui_Example = GuiExampleCode(root)
root.mainloop()
