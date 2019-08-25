import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

timestamps = []
temperatures = []
pressures = []

with open('data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    counter = 0
    for row in plots:
        counter += 1
        if(counter <= 2):
            continue
            # del timestamps[0]
        # timestamp = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
        if(len(timestamps) >= 100):
            timestamps.pop(0)
            temperatures.pop(0)
            pressures.pop(0)
        timestamps.append(row[0][11:])
        temperatures.append(float(row[1]))
        pressures.append(float(row[2]))


def animate(i):
    graph_data = open('data.csv','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)
