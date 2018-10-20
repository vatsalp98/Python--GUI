#Making a proper window of a normal Software

from tkinter import *

def doNothing():
    print("Jeez! Alright I won't do anything.")

def CopyFunction():
    status.config(text="Copied")

def PrintFunction():
    status.config(text="Printed")

root = Tk()
root.geometry("500x300")
# Menu
menubar = Menu(root)
root.config(menu=menubar)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project", command=doNothing)
subMenu.add_command(label="New", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.destroy)

EditMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu=EditMenu)
EditMenu.add_command(label="New", command=doNothing)


#Toolbar

toolbar = Frame(root,bg="blue")
copybtn = Button(toolbar, text="Copy", command=CopyFunction)
printbtn = Button(toolbar, text="Print", command=PrintFunction)

copybtn.pack(side=LEFT, padx=2, pady=2)
printbtn.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

#StatusBar

status = Label(root, text="Preparing the document...", bd=1, relief=SUNKEN, anchor=W) #relief makes it look like a statusbar
status.pack(side=BOTTOM, fill=X)


root.mainloop()
