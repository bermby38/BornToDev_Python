orderList = []

def showmenu():
    print("Dev Kitchen".center(30,"-"))

def orderfood():
    while True:
        orderName = input("Please Enter Menu : ")
        if(orderName.lower() == "exit"):
            break
        else:
            orderPrice = int(input("Price : "))
            orderList.append([orderName,orderPrice])
            #priceList.append(int(menuPrice))

def printbill():
    print("My food".center(30,"-"))
    for i in range(len(orderList)):
        print(orderList[i][0],orderList[i][1])
    print("Total",sumbill())

def sumbill():
    sum = 0
    for i in range(len(menuList)):
        sum += menuList[i][1]
    return sum

orderfood()
printbill()
