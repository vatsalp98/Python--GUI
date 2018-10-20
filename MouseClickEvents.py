from tkinter import *

root = Tk()

def leftClick(event):
    print("Left")
def rightClick(event):
    print("Right")
def MiddleClick(event):
    print("MiddleScroll")

frame = Frame(root, width=300, height=250, bg="black")
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-3>",rightClick)
frame.bind("<Button-2>",MiddleClick)
frame.pack()


root.mainloop()