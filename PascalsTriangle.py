numbers = [3, 10, 1, 7, 8, 9]

sum=0
for i in range (0, len(numbers)):
  sum = sum + numbers[i]

max=numbers[0]
for i in range (1, len(numbers)):
    if numbers[i]>max:
        max=numbers[i]

min=numbers[0]
for i in range (1, len(numbers)):
    if numbers[i]<min:
        min=numbers[i]

evencount=0
oddcount=0
for i in range (0, len(numbers)):
    if numbers[i]%2==0:
        evencount = evencount + 1
    else:
        oddcount = oddcount + 1


print(numbers[1])
print(len(numbers))
print("sum = " + str(sum))
print("biggest number is " + str(max))
print("smallest number is " + str(min))
print("there are " + str(evencount) + " even numbers")
print("there are " + str(oddcount) + " odd numbers")

def printarray(arr):
    for i in range (0, len(arr)):
      print(str(arr[i]) + " ", end='')
    print()

a=[1]
printarray(a)

for lines in range (0,7):
    b=[1]
    for i in range (0,len(a)-1):
        x=a[i]+a[i+1]
        b.append(x)
    b.append(1)
    printarray(b)
    a=b
