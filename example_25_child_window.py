from Tkinter import *

class Example(Frame):
	counter = 0
	def __init__(self,parent):
		Frame.__init__(self,parent,background="white")
		self.parent = parent 
		self.initUI()
	
	def initUI(self):
		self.parent.title("Parent Window")
		self.pack(fill=BOTH , expand = 1)
		self.button = Button(self,text="Create new window", command=self.createWindow)
		self.button.pack(side="top")
		self.button1 = Button(self,text="Print Text",command=self.printText)
		self.button1.pack(side="left")

	def createWindow(self):
		self.counter += 1
		self.parentWindowObject = Toplevel(self)
		self.parentWindowObject.wm_title("Window #%s"%self.counter)
		self.label = Label(self.parentWindowObject,text="This is window #%s"%self.counter)
		self.label.pack(side="top",fill="both",expand=True , padx=100 , pady=100)
	def printText(self):
		print "Hello You Cliked Me!!!"

if __name__ == '__main__':
	root = Tk()
	root.geometry("250x250+300+300")
	application = Example(root)
	root.mainloop()

	
