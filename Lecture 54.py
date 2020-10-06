def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    while usernameInput != "admin" or passwordInput != "1234":
        print("--Username or Password wrong--")
        usernameInput = input("Username : ")
        passwordInput = input("Password : ")
    return True

def showMenu():
    print("---ABC Shop---")
    print("1. Calculate VAT 7%")
    print("2. Calculate Price")
    selectMenu()

def selectMenu():
    inputNumber = input("Select Function :")
    if inputNumber == "1":
        inputPrice = int(input("Input price : "))
        print(vatCalculate(inputPrice))
    elif inputNumber == "2":
        priceCalculate()
    else:
        print("---Wrong Number---")
        showMenu()

def vatCalculate(totalPrice):

    totalPrice = totalPrice + (totalPrice*0.07)
    return totalPrice

def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    print(vatCalculate(price1 + price2))


if login():
    print("Login Succeed")
    showMenu()
