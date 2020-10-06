def vatCalculate(price):
    price = price + (price*7/100)
    return price

inputPrice = int(input("Input price : "))
print(vatCalculate(inputPrice))