import matplotlib.pyplot as plt
import csv
from datetime import datetime
import time

def UTC_timestamp():
    UTC_timestamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%s')[0:-7]
    return UTC_timestamp

def parseFile():

    timestamps = []
    pressures = []
    temperatures = []

    with open('data.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        counter = 0
        for row in plots:
            counter += 1
            if(counter <= 2):
                continue
            timestamp = datetime.timestamp(datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f'))
            if(len(timestamps) >= 100):
                timestamps.pop(0)
                temperatures.pop(0)
                pressures.pop(0)
            # timestamps.append(row[0][11:])
            timestamps.append(timestamp)
            pressures.append(float(row[1]))
            temperatures.append(float(row[2]))

    csvfile.close()

    plt.clf()

    plt.title(str(UTC_timestamp()))
    plt.xlabel('Timestamps')
    plt.ylabel('Temperature')
    plt.subplot(211)
    plt.plot(timestamps, temperatures, 'k-')
    plt.plot(timestamps, temperatures, 'r.')

    plt.title(str(UTC_timestamp()))
    plt.xlabel('Timestamps')
    plt.ylabel('Barometer')
    plt.subplot(212)
    plt.plot(timestamps, pressures, 'k-')
    plt.plot(timestamps, pressures, 'b.')

    plt.draw()
    plt.pause(0.1)

plt.show(block=True) # block=True lets the window stay open at the end of the animation.

while True:
    # Code executed here
    try:
        parseFile()
    except Exception as e:
        print(e)
        plt.close()

    time.sleep(1)
