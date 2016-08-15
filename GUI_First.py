# Import the tkinter library
from tkinter import *
import tkinter.messagebox

# Definition of the root window
root = Tk()

# Label definitions
#label_1 = Label(root, text="Name")
#label_2 = Label(root, text="Password")
#entry_1 = Entry(root)
#entry_2 = Entry(root)

#label_1.grid(row=0, sticky=E)
#label_2.grid(row=1, sticky=E)
#entry_1.grid(column=1, row=0)
#entry_2.grid(column=1, row=1)

#c = Checkbutton(root, text="Keep me logged in")
#c.grid(columnspan=2)

# Functions
def printName():
    print("Hello world")

# Buttons
#button_1 = Button(root, text="Print hello", command=printName)
#button_1.grid(row=3)

# Functions 2
def printName2(event):
    print("Hello world 2")

# Buttons
#button_2 = Button(root, text="Print other hello")
#button_2.bind("<Button-1>",printName2)
#button_2.grid(row=3, column=1)

# Functions 3
def rightClick(event):
    print("Right")

#button_3 = Button(root, text="Print other hello")
#button_3.bind("<Button-3>",rightClick)
#button_3.grid(row=3, column=3)

# Frames
#frame = Frame(root, width=300, height=200)
#frame.bind("<Button-3>",rightClick)
#frame.pack()

# Classes
class OcButtons:

    def __init__(self,master):
        frame=Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("It works!")
# Calls the class
#b=OcButtons(root)

# Menus
def doNothing():
    print("ok ok I won't...")

menu=Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)

# Toolbar
toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar,text="Insert image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar,text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# Status bar
status = Label(root, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# Pop-up's
#tkinter.messagebox.showinfo("Window Title", "blah blah")

#answer = tkinter.messagebox.askquestion('Question 1','With cheesse?')
#if answer == 'yes':
#    print('bork')

# Canvas
canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0,0,200,50)
redLine = canvas.create_line(0,100,200,50,fill="red")
greenBox = canvas.create_rectangle(25,25,130,60,fill="green")
canvas.delete(redLine)
canvas.delete(ALL)

photo = PhotoImage(file="Captura.png")
label = Label(root, image=photo)
label.pack()

# Starts the window (I guess)
root.mainloop()