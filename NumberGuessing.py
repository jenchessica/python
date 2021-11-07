lower = 1
upper = 2000000
print("Think of a number between " + str(lower) + " and " + str(upper))

middle=0
while True:
    lastmiddle = middle
    middle = (lower + upper)//2
    if middle == lastmiddle:
        middle = middle + 1
    print("My guess is " + str(middle))
    highlow = input('Is my guess too high or too low?')
    if highlow == "high":
        upper = middle
    elif highlow == "low":
        lower = middle
    elif highlow == "neither":
        break

print("YAYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY!!!")

