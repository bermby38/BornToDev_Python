from tkinter import *


def leftclickbutton(event):
    print(textboxWeight.get())


mainWindow = Tk()

labelHeight = Label(mainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0, column=0)
textboxHeight = Entry(mainWindow)
textboxHeight.grid(row=0, column=1)
labelWeight = Label(mainWindow, text="น้ำหนัก (kg.)")
labelWeight.grid(row=1, column=0)
textboxWeight = Entry(mainWindow)
textboxWeight.grid(row=1, column=1)
buttonCalculate = Button(mainWindow, text="คำนวณ BMI")
buttonCalculate.grid(row=2, column=0)
buttonCalculate.bind('<Button-1>', leftclickbutton)

mainWindow.mainloop()
