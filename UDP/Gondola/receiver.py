import socket
import struct

MCAST_GRP = "224.168.2.9"
MCAST_PORT = 4446
IS_ALL_GROUPS = True

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if IS_ALL_GROUPS:
    # on this port, receives ALL multicast groups
    sock.bind(('', MCAST_PORT))
else:
    # on this port, listen ONLY to MCAST_GRP
    sock.bind((MCAST_GRP, MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print "Listening..."
while True:
    string = sock.recv(10240)
    tempo_Data = map(str.strip, string.split(','))
    shouldTerminate = int(tempo_Data[4])
    if(shouldTerminate > 0):
        print "Should terminate!", shouldTerminate
    else:
        print "what is this"
