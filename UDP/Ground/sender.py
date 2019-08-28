import socket
import datetime, time
import sys

MCAST_GRP = "10.90.35.148"
MCAST_PORT = 5002
# regarding socket.IP_MULTICAST_TTL
# ---------------------------------
# for all packets sent, after two hops on the network the packet will not
# be re-sent/broadcast (see https://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
MULTICAST_TTL = 4

terminate_val = 0

try:
    terminate_val = sys.argv[1]
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
# TELEMETRY DATA:
# 0 ... do not terminate
# 1 ... terminate
MSG.append(str(terminate_val))

# Create CSV string
MSG_CSV = ",".join(MSG)
print "Sending string: ", MSG_CSV

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
sock.sendto(MSG_CSV, (MCAST_GRP, MCAST_PORT))
