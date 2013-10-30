#!/usr/bin/env python
import hubo_ach
import ach
import sys
import time
from ctypes import *
import socket
import cv2.cv as cv
import cv2
import numpy as np

HUBO_CHAN_VIEW   = 'hubo-view'


# CV setup 
cv.NamedWindow("w2", cv.CV_WINDOW_AUTOSIZE)
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
#    f, img = capture.read()
    img = np.zeros((newx,newy,3), np.uint8)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    vid = cv2.resize(gray_image,(newx,newy))

    [status, framesize] = v.get(vid, wait=True, last=False)
    if status == ach.ACH_OK or status == ach.ACH_MISSED_FRAME:
        cv2.imshow("w2", vid)
        cv2.waitKey(10)
    else:
        raise ach.AchException( v.result_string(status) )
    i=i+1
    print i
    time.sleep(0.1)
    

