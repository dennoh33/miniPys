from tkinter import *

root = Tk()
root.title("Basic Calculator")

e = Entry(width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def click_button(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clear_button():
    e.delete(0, END)


def add_button():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def subtract_button():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def multiply_button():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def divide_button():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def equal_button():

    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        sum = f_num + int(second_number)
        e.insert(0, sum)

    elif math == "subtraction":
        difference = f_num - int(second_number)
        e.insert(0, difference)

    elif math == "multiplication":
        product = f_num * int(second_number)
        e.insert(0, product)

    elif math == "division":
        quotient = f_num / int(second_number)
        e.insert(0, quotient)


button_1 = Button(root, text="1", padx="40", pady="20", command=lambda: click_button(1))
# lambda is used when i want to pass something to a button
button_2 = Button(root, text="2", padx="40", pady="20", command=lambda: click_button(2))
button_3 = Button(root, text="3", padx="40", pady="20", command=lambda: click_button(3))

button_4 = Button(root, text="4", padx="40", pady="20", command=lambda: click_button(4))
button_5 = Button(root, text="5", padx="40", pady="20", command=lambda: click_button(5))
button_6 = Button(root, text="6", padx="40", pady="20", command=lambda: click_button(6))

button_7 = Button(root, text="7", padx="40", pady="20", command=lambda: click_button(7))
button_8 = Button(root, text="8", padx="40", pady="20", command=lambda: click_button(8))
button_9 = Button(root, text="9", padx="40", pady="20", command=lambda: click_button(9))

button_0 = Button(root, text="0", padx="40", pady="20", command=lambda: click_button(0))
button_add = Button(root, text="+", padx=39, pady=20, command=add_button)
button_equal = Button(root, text="=", padx=91, pady=20, command=equal_button)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=clear_button)


button_subtract = Button(root, text="-", padx="40", pady="20", command=subtract_button)
button_multiply = Button(root, text="*", padx="40", pady="20", command=multiply_button)
button_divide = Button(root, text="/", padx="40", pady="20", command=divide_button)


# putting buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)


button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
