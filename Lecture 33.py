price = 0.00
vat = 7
priceIncludeVat = 0.00

price = float(input("Input price : "))
priceIncludeVat = price * (vat+100) /100

print(priceIncludeVat)