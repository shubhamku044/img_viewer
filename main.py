from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")

img1 = ImageTk.PhotoImage(Image.open('img1.jpg'))
img2 = ImageTk.PhotoImage(Image.open('img2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('img3.jpg'))
img4 = ImageTk.PhotoImage(Image.open('img4.jpg'))
img5 = ImageTk.PhotoImage(Image.open('img5.jpg'))
img6 = ImageTk.PhotoImage(Image.open('img6.jpg'))

images = [img1, img2, img3, img4, img5, img6]
number = 0

my_label = Label(root, image=images[number])
my_label.grid(row=0, column=0, columnspan=3)

num_label = Label(root, text = f"Image 1 out of 6", bd=0.5, relief=SUNKEN, anchor=E)
num_label.grid(row=2, column=0, sticky=W+E, columnspan=3)


def show_img_no(num):
    global num_label
    num_label.grid_forget()
    num_label = Label(root, text=f"Image {num + 1} out of 6", bd=0.5, relief=SUNKEN, anchor=E)
    num_label.grid(row=2, column=0, sticky=W+E, columnspan=3)

def check_button_state():
    global number
    if number == 0:
        bwd_button = Button(root, text="<<", command=lambda: bwd(number), state=DISABLED)
        bwd_button.grid(row=1, column=0)
    else:
        bwd_button = Button(root, text="<<", command=lambda: bwd(number))
        bwd_button.grid(row=1, column=0)

    if number == 5:
        fwd_button = Button(root, text=">>", command=lambda: fwd(number), state=DISABLED)
        fwd_button.grid(row=1, column=2)
    else:
        fwd_button = Button(root, text=">>", command=lambda: fwd(number))
        fwd_button.grid(row=1, column=2)

def fwd(img_no):
    global fwd_button
    global my_label
    global number

    img_no += 1
    number = img_no
    my_label.grid_forget()
    my_label = Label(root, image=images[img_no])
    my_label.grid(row=0, column=0, columnspan=3)
    check_button_state()
    show_img_no(number)


def bwd(img_no):
    global bwd_button
    global my_label
    global number

    img_no -= 1
    number = img_no
    my_label.grid_forget()
    my_label = Label(root, image=images[img_no])
    my_label.grid(row=0, column=0, columnspan=3)
    check_button_state()
    show_img_no(number)

check_button_state()

button_quit = Button(root, text="Quit", command=root.quit)
button_quit.grid(row=1, column=1)

root.mainloop()