target="power"
done=False
count=1

while not done:
    guess=input('Your guess ' + str(count) + ": ")

    # First build the character count dictionary of the target
    charcount={}
    for i in range(0, len(target)):
        if target[i] in charcount:
            charcount[target[i]]=charcount[target[i]]+1
        else:
            charcount[target[i]]=1
    #print(charcount)

    # Second, cancel out the count of the exact match.
    # This will leave us with a correct dictionary for third step.
    for i in range(0, len(guess)):
        if guess[i]==target[i]:
            charcount[guess[i]]=charcount[guess[i]]-1

    # Third, scan through target and guess, then give hint
    for i in range(0, len(guess)):
        if guess[i]==target[i]:
            print("[" + guess[i] + "]", end="")
        else:
            if guess[i] in charcount and charcount[guess[i]]>0:
                print("(" + guess[i] + ")", end="")
                charcount[guess[i]]=charcount[guess[i]]-1
            else:
                print(" " + guess[i] + " ", end="")

    # print(charcount)

    print("")
    count=count+1
    done=(target==guess)

