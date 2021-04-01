from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="red")
e.pack()


def myClick():
    msg = f"Hey {e.get()}"
    myLabel = Label(root, text=msg)
    myLabel.pack()


myButton = Button(root, text="Enter your name.", command=myClick)
myButton.pack()

root.mainloop()
