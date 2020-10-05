inputRound = int(input("Please input number :"))
sum = 0
for x in range(inputRound):
    inputNumber = int(input("x"+str(x+1)+" : "))
    sum += inputNumber

print("SUM = ", sum)