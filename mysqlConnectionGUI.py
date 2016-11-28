#author = Dipayan Dutta
'''code to connect python with mysql database using Tkinter module i.e. GUI'''

import MySQLdb
import Tkinter
import tkMessageBox


class connectMySQL:
    def __init__(self,parent):
        self.parent = parent

        self.username = Tkinter.Label(parent,text="username")
        self.username.pack()

        self.usernameEntry = Tkinter.Entry(parent,bd=5,width=10)
        self.usernameEntry.pack()

        self.password = Tkinter.Label(parent,text="password")
        self.password.pack()

        self.passwordEntry = Tkinter.Entry(parent,show="*",bd=5,width=10)
        self.passwordEntry.pack()

        self.loginButton = Tkinter.Button(parent,text="Login",command = self.check)
        self.loginButton.pack()

    def check(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        usernameLength = len(username)
        passwordLength = len(password)

        
        try:
            if usernameLength==0 or passwordLength==0:
                tkMessageBox.showinfo("Please provide username and password")
            else:
                connection = MySQLdb.connect(host='localhost',user=username,passwd=password,db='python')
                if connection:
                    tkMessageBox.showinfo("Successfully Connected to the database")
                    print "Database connection done"
                if not connection:
                    tkMessageBox.showinfo("Unable to connect Database")
                    print "Unbale to connect database "
        except:
            print "Please check!"

root = Tkinter.Tk()
connect = connectMySQL(root)
root.mainloop()
    
