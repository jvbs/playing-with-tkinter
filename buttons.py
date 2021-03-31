from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Button clicked")
    myLabel.pack()


# myBtn = Button(root, text="Click me!")
#myBtn = Button(root, text="Click me!", state=DISABLED)
myBtn = Button(root, text="Click me!", padx=50, pady=50, command=myClick)
myBtn2 = Button(root, text="Click me!", padx=50,
                pady=50, fg="green", bg="yellow")
myBtn.pack()
myBtn2.pack()

root.mainloop()
