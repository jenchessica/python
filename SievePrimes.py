a = []
for i in range (0, 101):
    a.append(True)

for i in range (2, 101):
    if a[i] == True:
        print(i)
        for j in range (2*i, 101):
            if j % i == 0:
                a[j] = False

