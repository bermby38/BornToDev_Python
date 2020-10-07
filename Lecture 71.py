menuList = []
priceList = []

def orderfood():
    while True:
        menuName = input("Please Enter Menu : ")
        if(menuName.lower() == "exit"):
            break
        else:
            menuPrice = input("Price : ")
            menuList.append(menuName)
            priceList.append(int(menuPrice))

def printbill():
    for i in range(len(menuList)):
        print(menuList[i], priceList[i])
    print("Total",sum(priceList))

orderfood()
printbill()
