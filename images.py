from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Icons")
root.iconbitmap("happyico.ico")

my_img = ImageTk.PhotoImage(Image.open("images/pic1.JPG"))
my_img1 = ImageTk.PhotoImage(Image.open("images/DSC_0199.JPG"))
my_img2 = ImageTk.PhotoImage(Image.open("images/DSC_0203.JPG"))
my_img3 = ImageTk.PhotoImage(Image.open("images/DSC_0206.JPG"))

image_list = [my_img, my_img1, my_img2, my_img3]

my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: backward(image_number-1))
    my_label.grid(row=0, column=0, columnspan=3)


def backward():
    global my_label
    global button_forward
    global button_back


button_back = Button(root, text="<<", command=backward)
button_forward = Button(root, text=">>", command=lambda: forward(2))
button_quit = Button(root, text="Exit", command=root.quit)

button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=1)
button_quit.grid(row=1, column=2)

root.mainloop()
