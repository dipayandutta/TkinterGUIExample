from Tkinter import *

class Example(Frame):

  def __init__(self,parent):
    Frame.__init__(self,parent)
    self.parent = parent
    self.initUI()
    self.loadIcons()
    self.menus()
    self.textpad()

  def initUI(self):
    self.parent.title('Project-01')
    #self.pack(fill=BOTH,expand=True)

  def loadIcons(self):
    self.new_file_icon = PhotoImage(file='icons/new_file.gif')
    self.open_file_icon = PhotoImage(file='icons/open_file.gif')
    self.save_file_icon = PhotoImage(file='icons/save.gif')
    self.cut_icon = PhotoImage(file='icons/cut.gif')
    self.copy_icon = PhotoImage(file='icons/copy.gif')
    self.paste_icon = PhotoImage(file='icons/paste.gif')
    self.undo_icon = PhotoImage(file='icons/undo.gif')
    self.redo_icon = PhotoImage(file='icons/redo.gif')

  def menus(self):

    '''Creating Menubar'''
    menubar = Menu(self.parent)

    '''Creating File menu and its items '''
    file_menu = Menu(menubar,tearoff=0)
    file_menu.add_command(label='New',accelerator='Ctrl+N',compound='left',
                         image=self.new_file_icon)
    file_menu.add_command(label='Open',accelerator='Ctrl+O',compound='left',
                         image=self.open_file_icon)
    file_menu.add_command(label='Save',accelerator='Ctrl+S',compound='left',
                         image=self.save_file_icon)
    file_menu.add_command(label='Save as',accelerator='Ctrl+Shift+S')
    file_menu.add_separator()
    file_menu.add_command(label='Exit',accelerator='Alt+F4')
    menubar.add_cascade(label='File',menu=file_menu) # Adding file menu to the menu bar

    edit_menu = Menu(menubar,tearoff=0)
    edit_menu.add_command(label='Undo',accelerator='Ctrl+z',compound='left',
                         image=self.undo_icon)
    edit_menu.add_command(label='Redo',accelerator='Ctrl+R',compound='left',
                         image=self.redo_icon)
    edit_menu.add_separator()
    edit_menu.add_command(label='Copy',accelerator='Ctrl+C',compound='left',
                         image=self.copy_icon)
    edit_menu.add_command(label='Cut',accelerator='Ctrl+X',compound='left',
                         image=self.cut_icon)
    edit_menu.add_command(label='Paste',accelerator='Ctrl+V',compound='left',
                         image=self.paste_icon)
    edit_menu.add_separator()
    edit_menu.add_command(label='Find',underline=0,accelerator='Ctrl+F')
    edit_menu.add_separator()
    edit_menu.add_command(label='Select All',accelerator='Ctrl+Shift+A')
    menubar.add_cascade(label='Edit',menu=edit_menu)

    self.parent.config(menu=menubar)



  def textpad(self):
      context_text = Text(self.parent,wrap='word')
      context_text.pack(fill=BOTH,expand=True)
      scroll_bar = Scrollbar(context_text)
      context_text.configure(yscrollcommand=scroll_bar.set)
      scroll_bar.config(command=context_text.yview)
      scroll_bar.pack(side='right',fill='y')

def main():
  root = Tk()
  app = Example(root)
  root.geometry("250x250+300+300")
  root.mainloop()

if __name__ == '__main__':
  main()
