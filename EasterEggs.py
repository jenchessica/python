def exists(arr, target):
    for i in range (0, len(arr)):
        if arr[i]==target:
            print(str(target) + " exists")

exists([3, -1, 8, 5, 7, 10], 8)
exists([3, -1, 8, 5, 7, 10], 2)
exists([3, -1, 8, 5, 7, 10], -1)


def findegg(locations):
    eggcount=0
    for i in range (0, len(locations)):
        if "@" in locations[i]:
            eggcount=eggcount+1
            print("You found an egg in the " + locations[i].replace("@", ""))
    print(str(eggcount) + " eggs found")



findegg(["kitch@en", "book", "bedroom", "s@ofa"])
