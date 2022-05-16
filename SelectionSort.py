def printarray(arr):
    for i in range (0, len(arr)):
         print(str(arr[i]) + " ", end='')
    print(" ")


numbers=[3, -7, 4, -2, 0, -5]

for targetspot in range (0, len(numbers)-1):
    print("Target Spot = " + str(targetspot))
    minvalue=numbers[targetspot]
    minspot=targetspot

    for i in range(targetspot+1, len(numbers)):
        if numbers[i]<minvalue:
            minvalue=numbers[i]
            minspot=i

    temp=numbers[targetspot]
    numbers[targetspot]=numbers[minspot]
    numbers[minspot]=temp

    printarray(numbers)

    print("----")
