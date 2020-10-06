def addNumber(x,y):
    print(x+y)
def minusNumber(x,y):
    print(x-y)
def multiplyNumber(x,y):
    print(x*y)
def divideNumber(x,y):
    print(x/y)

inputX = (int(input("Input x : ")))
inputOperand = input("Input Operand : ")
inputY = (int(input("Input y : ")))

if inputOperand == "+":
    addNumber(inputX,inputY)
elif inputOperand == "-":
    minusNumber(inputX, inputY)
elif inputOperand == "*":
    multiplyNumber(inputX, inputY)
elif inputOperand == "/":
    divideNumber(inputX, inputY)
