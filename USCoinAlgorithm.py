CoinDenominations = [25, 10, 5, 1]
CoinNames = ["Quarter(s)", "Dime(s)", "Nickel(s)", "Cent(s)"]
v = 723
totalNum = 0
print(str(v) + " cents needs:")
for i in range (0, len(CoinDenominations)):
    num=v//CoinDenominations[i]
    v=v%CoinDenominations[i]
    if num>0:
        totalNum = totalNum+num
        print(str(num) + " " + CoinNames[i])
print("Total Coin Count is: " + str(totalNum))

