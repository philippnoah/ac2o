import socket
import datetime
import time
import csv
import sys
import os

ACTUAL_IP = "172.20.4.230"
# 230-239

UDP_IP = ""
UDP_PORT = 5002

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

def UTC_timestamp():
    UTC_timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%s')[0:-7]
    return UTC_timestamp

counter = 0
max_lines = 10000
start_time = time.time()

try:
    while True:
        string, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        tempo_data = map(str.strip, string.split(','))
        try:
            if float(tempo_data[4]) == float(69420):
                print "------ Systems [OFF] ------ "
            elif float(tempo_data[4]) == float(290100):
                print "------ Systems [ON] ------ "
            data = [tempo_data[2], tempo_data[4], tempo_data[5]]
        except Exception as e:
            print (string)
            print (e)
            continue
        print data
        counter += 1
        if not os.path.exists('data.csv'):
            with open('data.csv', 'w+') as writeFile:
                writer = csv.writer(writeFile)
                start_time = time.time()
                writer.writerow([str(start_time), "Created on: ", UTC_timestamp()])
                writer.writerow(["Timestamp", "Barometer", "Temperature"])
            writeFile.close()
        with open('data.csv', 'a') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(data)
            if(counter % max_lines == 0):
                print counter
                os.rename("data.csv", "./archive/"+str(start_time).replace(".", "_")+".csv")
        writeFile.close()
except Exception as e:
    print("Recording stopped: ", e)
finally:
    try:
        os.mkdir("archive")
    except Exception as e:
        print(e)
    finally:
        os.rename("data.csv", "./archive/"+str(start_time).replace(".", "_")+".csv")
