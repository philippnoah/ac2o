import socket
import struct
import matplotlib.pyplot as plt
import datetime, time
import numpy as np
import csv
import time
import sys, signal
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
        tempo_Data = map(str.strip, string.split(','))
        data = [tempo_Data[2], tempo_Data[4], tempo_Data[5]]
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
finally:
    try:
        os.mkdir("archive")
    finally:
        os.rename("data.csv", "./archive/"+str(start_time).replace(".", "_")+".csv")
