import socket
import time

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
i = 0
while True:
    sock.sendto("robot", (MCAST_GRP, MCAST_PORT))
    print i
    i=i+1
    time.sleep(1)
    

