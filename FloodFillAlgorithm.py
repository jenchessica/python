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

drawfig(grid)
