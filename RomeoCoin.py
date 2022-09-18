CoinDenominations = [1, 7, 9]
v = 15
f = [0]*(v+1)

for n in range (1, v+1):
    print("f[" + str(n) + "] = min(" , end='')
    currentmin=1000000
    everprinteditem=False
    for i in range (0, len(CoinDenominations)):
        if n>=CoinDenominations[i]:
            if everprinteditem:
                print(",f(" + str(n-CoinDenominations[i]) + ")", end='')
            else:
                print("f(" + str(n-CoinDenominations[i]) + ")", end='')
                everprinteditem=True

            if f[n-CoinDenominations[i]]<currentmin:
                currentmin=f[n-CoinDenominations[i]]

    f[n]=currentmin+1
    print(")+1="+str(f[n]))
