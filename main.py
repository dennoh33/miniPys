from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="This is a drake world!")

# shoving widget to screen
myLabel1.pack()
myLabel2.pack()

# button function


def myclick():
    mylabel3 = Label(root, text=e.get())
    mylabel3.pack()


myButton = Button(root, text="SUBMIT", padx=10, pady=10, command=myclick)
myButton.pack()


e=Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter text to submit: ")
e.get()


root.mainloop()
