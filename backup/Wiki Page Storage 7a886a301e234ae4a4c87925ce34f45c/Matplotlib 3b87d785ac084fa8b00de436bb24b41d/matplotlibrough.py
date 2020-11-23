import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style



# define constants
weight = 0.5
goal_pred = 0.8
input = -0.5

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
# create 1000 equally spaced points between -10 and 10
# x = np.linspace(-1, +1, 1000)
# calculate the y value for each element of the x vector
# y = (input**2)*(x**2) + goal_pred**2-2 * input * goal_pred*weight
# fig, ax = plt.subplots()
# ax.plot(x, y)


# gradient descent
def animate(i):
    global weight
    xa = [weight]
    ya = []
    for i in range(20):
        pred = input * weight
        error = (pred - goal_pred) ** 2
        ya.append(error)
        direction_and_amount = (pred - goal_pred) * (input)
        if i > 0:
            ax1.clear()
            ax1.plot(xa,ya)
        weight = weight - direction_and_amount
        xa.append(weight)
        print("Error:" + str(error) + " Prediction:" + str(pred))
        


ani=animation.FuncAnimation(fig,animate,interval=200)
plt.show()





def animate(i):
	graph_data = open('example.txt', 'r').read()
	lines = graph_data.split('\n')
	xs = []
	ys = []]
	for line in lines:
	if len(line) > 1:
	x, y = line.split(',')
	xs. append(x)
	ys. append(y)
	ax1.clear()
	axl.plot(xs, ys)
