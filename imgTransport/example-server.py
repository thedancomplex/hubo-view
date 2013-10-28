#
#   Weather update server
#   Binds PUB socket to tcp://*:5556
#   Publishes random weather updates
#

import zmq
import random
import cv2.cv as cv
import cv2

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
#capture = cv.CaptureFromCAM(0)
capture = cv2.VideoCapture(0)


while True:
    zipcode = random.randrange(1,100000)
    temperature = random.randrange(1,215) - 80
    relhumidity = random.randrange(1,50) + 10

    # Get Frame
#    frame = cv.QueryFrame(capture)
    f, img = capture.read()
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    cv.ShowImage("w1", gray_image)
    cv2.imshow("w1", gray_image)
    cv2.waitKey(10)
#    c = cv.WaitKey(10)
#    if (cv2.waitKey (5) != -1):
#        break;

#    socket.send(frame)


#    socket.send("%d %d %d" % (zipcode, temperature, relhumidity))
