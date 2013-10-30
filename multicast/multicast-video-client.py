import socket
import sys
import struct
import cv2.cv as cv
import cv2
import numpy as np

# Open viewing window
cv.NamedWindow("w2", cv.CV_WINDOW_AUTOSIZE)


MCAST_GRP = '226.1.1.1'
MCAST_PORT = 11001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    tmp = sock.recv(22000)
#    tmp = np.array(tmp)
    print sys.getsizeof(tmp)
    tmp = np.fromstring(tmp, np.uint8)
    tmp = np.reshape(tmp,(120,180))
    cv2.imshow("w2", tmp)
    cv2.waitKey(10)
### np.genfromtxt
### http://stackoverflow.com/questions/7497328/reading-ascii-file-in-python-numpy-array

###http://stackoverflow.com/questions/14584566/transferring-image-files-from-sever-to-client-using-python-socket-programming

### http://stackoverflow.com/questions/18817650/python-simplecv-tostring-back-to-image
    print sys.getsizeof(tmp)
