menuList = []
#priceList = []

def orderfood():
    while True:
        menuName = input("Please Enter Menu : ")
        if(menuName.lower() == "exit"):
            break
        else:
            menuPrice = int(input("Price : "))
            menuList.append([menuName,menuPrice])
            #priceList.append(int(menuPrice))

def printbill():
    print("My food".center(30,"-"))
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
    print("Total",sumbill())

def sumbill():
    sum = 0
    for i in range(len(menuList)):
        sum += menuList[i][1]
    return sum

orderfood()
printbill()
