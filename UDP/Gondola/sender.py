import socket
import datetime, time
import random
import sys

def send(b, t):

    b_val = b
    t_val = t

    try:
        b_val = float(sys.argv[1]) + random.randint(0,5)
        t_val = float(sys.argv[2]) + random.randint(0,5)
    except:
        None

    # Init Message
    MSG = []
    # SOURCE: leave blank
    MSG.append("")
    # MISSION TIMESTAMP: leave blank
    MSG.append("")
    # SUB-SYSTEM TIMESTAMP:
    UTC_timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%s')[0:-7]
    MSG.append(UTC_timestamp)
    # PACKET ID: TBD
    MSG.append("AC2Oxx")
    # SOFTWARE ID, omitted entirely in th example
    # MSG[0] = ""
    # TELEMETRY DATA
    # Simulate barometer
    MSG.append(str(b_val))
    # Simulate temperature
    MSG.append(str(t_val))

    # Create CSV string
    MSG_CSV = bytes(",".join(MSG), 'UTF-8')
    print(MSG_CSV)

    MCAST_GRP = "10.90.34.148"
    MCAST_PORT = 5002
    # regarding socket.IP_MULTICAST_TTL
    # ---------------------------------
    # for all packets sent, after two hops on the network the packet will not
    # be re-sent/broadcast (see https://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
    MULTICAST_TTL = 4

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
    sock.sendto(MSG_CSV, (MCAST_GRP, MCAST_PORT))

print("Start sending...")
while True:
    # Code executed here
    send(1, 2)
    time.sleep(3)
