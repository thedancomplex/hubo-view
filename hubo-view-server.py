#!/usr/bin/env python
import hubo_ach
import ach
import sys
import time
from ctypes import *
import socket
import cv2.cv as cv
import cv2


HUBO_CHAN_VIEW   = 'hubo-view-vid'


# CV setup 
###cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
#capture = cv.CaptureFromCAM(0)
capture = cv2.VideoCapture(0)

# added
##sock.connect((MCAST_GRP, MCAST_PORT))
newx = 180
newy = 120


v = ach.Channel(HUBO_CHAN_VIEW)
v.flush()
i=0
while True:
    # Get Frame
    f, img = capture.read()
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.resize(gray_image,(newx,newy))
###    cv2.imshow("w1", gray_image)
###    cv2.waitKey(10)

#    print sys.getsizeof(gray_image)
    v.put(gray_image)
    i=i+1
    print i
    time.sleep(0.1)
    

