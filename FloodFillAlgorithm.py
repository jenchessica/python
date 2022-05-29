from matplotlib import pyplot as plt, patches

def drawfig(grid):
    colors=['white', 'black', 'grey']
    figure, _ = plt.subplots()
    ax = plt.gca()
    ax.set_xlim([-20, 120])
    ax.set_ylim([-120, 20])

    for row in range (0, len(grid)):
        for col in range (0, len(grid[row])):
            ax.add_patch(patches.Rectangle((col*10, row*(-10)), 10, 10, edgecolor='grey', facecolor=colors[grid[row][col]], linewidth=2))

    plt.show()

def explorenewcell(grid,newrow,newcol,queue):
    if newrow>=0 and newrow<=9 and newcol>=0 and newcol<=9 and grid[newrow][newcol]==0:
        queue.append(newrow*10+newcol)


grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

queue = []
queue.append(3*10+2)

while len(queue)>0:
    cell = queue.pop(0)
    col = int(cell%10)
    row = int(cell/10)

    #process this cell

    #fill color
    grid[row][col]=2

    #explore
    explorenewcell(grid,row-1,col,queue)
    explorenewcell(grid,row+1,col,queue)
    explorenewcell(grid,row,col-1,queue)
    explorenewcell(grid,row,col+1,queue)

drawfig(grid)



