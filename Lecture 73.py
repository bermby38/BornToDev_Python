orderList = []
menuDict = {"ข้าวมันไก่":45, "ข้าวมันไก่ทอด":45, "ข้าวมันไก่ผสม":50}

def showmenu():
    print("Dev Kitchen".center(30,"-"))
    print(menuDict.keys())

def orderfood():
    while True:
        orderName = input("Please Enter Menu : ")
        if(orderName.lower() == "exit"):
            break
        else:
            orderPrice = menuDict[orderName]
            orderList.append([orderName,orderPrice])

def printbill():
    print("My food".center(30,"-"))
    for i in range(len(orderList)):
        print(orderList[i][0],orderList[i][1])
    print("Total",sumbill())

def sumbill():
    sum = 0
    for i in range(len(orderList)):
        sum += orderList[i][1]
    return sum

showmenu()
orderfood()
printbill()
