import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('16_data.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:   # takes care of possible empty line
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()

    # setting title must be done inside the animate function, otherwise will be cleared
    # by preceding instruction !
    plt.title('Dynamically add a line to the data file and save it to update the graph !')
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)  # assignement to a variable is required !
plt.show()