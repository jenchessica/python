import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(111, projection='3d')

n=3

for z in range (-n, n+1):
    for y in range (-n, n+1):
        for x in range (-n, n+1):
            if abs(x)+abs(y)+abs(z)<=n:
                ax.scatter(x,y,z, color = 'black')

ax.view_init(10, 20)
plt.show()
