from tkinter import *

def sayhello():
    print("Hello World")

MainWindow = Tk()
button1 = Button(MainWindow, text="Click Me", command=sayhello)
button1.place(x = 50, y =20)
MainWindow.mainloop()