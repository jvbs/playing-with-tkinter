from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# e.pack()


def clickBtnHandler(number):
    current = e.get()
    e.insert(0, str(current) + str(number))
    # e.delete(0, number)


# Define Buttons

# Number Buttons
btn1 = Button(root, text="1", padx=40, pady=20,
              command=lambda: clickBtnHandler(1))
btn2 = Button(root, text="2", padx=40, pady=20,
              command=lambda: clickBtnHandler(2))
btn3 = Button(root, text="3", padx=40, pady=20,
              command=lambda: clickBtnHandler(3))
btn4 = Button(root, text="4", padx=40, pady=20,
              command=lambda: clickBtnHandler(4))
btn5 = Button(root, text="5", padx=40, pady=20,
              command=lambda: clickBtnHandler(5))
btn6 = Button(root, text="6", padx=40, pady=20,
              command=lambda: clickBtnHandler(6))
btn7 = Button(root, text="7", padx=40, pady=20,
              command=lambda: clickBtnHandler(7))
btn8 = Button(root, text="8", padx=40, pady=20,
              command=lambda: clickBtnHandler(8))
btn9 = Button(root, text="9", padx=40, pady=20,
              command=lambda: clickBtnHandler(9))
btn0 = Button(root, text="0", padx=40, pady=20,
              command=lambda: clickBtnHandler(0))

# Operators
btnAdd = Button(root, text="+", padx=39, pady=20,
                command=lambda: clickBtnHandler())
btnEqual = Button(root, text="=", padx=91, pady=20,
                  command=lambda: clickBtnHandler())
btnClear = Button(root, text="Clear", padx=79,
                  pady=20, command=lambda: clickBtnHandler())

# Put the buttons on the screen
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column=0)

btnClear.grid(row=4, column=1, columnspan=2)
btnAdd.grid(row=5, column=0)
btnEqual.grid(row=5, column=1, columnspan=2)

root.mainloop()
