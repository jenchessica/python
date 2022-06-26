from matplotlib import pyplot as plt, patches

def drawbead(axes,radius,x,y, color):
    #draw first uncolored circle
    uncolored_circle = plt.Circle( (x, y), radius , fill = False )
    axes.add_artist(uncolored_circle)

    #draw second uncolored circle
    colored_circle = plt.Circle( (x, y), 0.5*radius, color=color)
    axes.add_artist(colored_circle)

def drawnecklace(arr,desc):
    #create axis
    figure, axes = plt.subplots()
    axes.set_aspect( 1 )
    r=0.05

    for i in range (0, len(arr)):
        x=i*2*r+r
        drawbead(axes,r,x,0.3, arr[i])

    #show
    plt.title(desc)
    plt.show()

def ispretty(arr):
    stack = []
    for i in range (0, len(arr)):
        if len(stack)>0 and arr[i]==stack[-1]:
            stack.pop()
        else:
            stack.append(arr[i])

    if len(stack)==0:
        return True
    else:
        return False

#drawbead(0.1, 0.3, 0.3, "r")

colors=["y", "r", "b", "m", "m", "b", "r", "y"]

x=ispretty(colors)

if x:
    drawnecklace(colors,'pretty')
else:
    drawnecklace(colors,'ugly')

