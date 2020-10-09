from tkinter import *


def sayHelloWorld():
    print("Hello World")


MainWindow = Tk()
text1 = Label(MainWindow, text="Hello World", width=20, fg="#FFFFFF", bg="#537D9D", font=("Helvetica,72")).grid(row=0, column=1)

MainWindow.mainloop()
