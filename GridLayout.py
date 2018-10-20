from tkinter import *

root = Tk()

def checkState():
    if var.get() == 1:
        print("Checkbox is checked")
    else:
        print("Not Checked")



label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")

entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, column=0, sticky=E)
label_2.grid(row=1, column=0, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

var = IntVar()
c = Checkbutton(root, text="Keep Me Logged in", command=checkState, variable=var)
c.grid(columnspan=2)

root.mainloop()