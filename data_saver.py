# values given from somewhere else
values = []

counter = 0
max_lines = 10000
start_time = time.time()

try:
    os.mkdir("archive")
except Exception as e:
    print(e)

try:
    while True:
        string, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        tempo_data = map(str.strip, string.split(','))
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
                os.rename("data.csv", "./archive/"+str(start_time).replace(".", "_")+".csv")
        writeFile.close()
except Exception as e:
    print("Recording stopped: ", e)
finally:
    os.rename("data.csv", "./archive/"+str(start_time).replace(".", "_")+".csv")
