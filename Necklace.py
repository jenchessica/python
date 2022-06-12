from matplotlib import pyplot as plt, patches

def drawbead(axes,radius,x,y, color):
    #draw first uncolored circle
    uncolored_circle = plt.Circle( (x, y), radius , fill = False )
    axes.add_artist(uncolored_circle)

    #draw second uncolored circle
    colored_circle = plt.Circle( (x, y), 0.5*radius, color=color)
    axes.add_artist(colored_circle)

def drawnecklace(arr):
    #create axis
    figure, axes = plt.subplots()
    axes.set_aspect( 1 )
    r=0.05

    for i in range (0, len(arr)):
        x=i*2*r+r
        drawbead(axes,r,x,0.3, arr[i])

    #show
    plt.title( 'Circle' )
    plt.show()

#drawbead(0.1, 0.3, 0.3, "r")

colors=["r", "b", "m", "y", "r", "b", "m", "y", "r", "b"]
drawnecklace(colors)


