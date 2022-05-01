def printarray(arr):
    for i in range (0, len(arr)):
         print(str(arr[i]) + " ", end='')
    print(" ")


numbers=[3, -7, 4, -2, 0, -5]

for upperlimit in range (len(numbers)-1, 0, -1):
    print("Upper limit = " + str(upperlimit))

    for i in range(0, upperlimit):
        print("i=" + str(i) + ": ", end='')
        if numbers[i]<numbers[i+1]:
            temp=numbers[i]
            numbers[i]=numbers[i+1]
            numbers[i+1]=temp
        printarray(numbers)

    print("----")




