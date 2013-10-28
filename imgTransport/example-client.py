#
#   Weather update client
#   Connects SUB socket to tcp://localhost:5556
#   Collects weather updates and finds avg temp in zipcode
#

import sys
import zmq
import cv2.cv as cv
import cv2

# Open viewing window
cv.NamedWindow("w2", cv.CV_WINDOW_AUTOSIZE)


#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print "Collecting updates from weather server..."
socket.connect ("tcp://localhost:5556")
#socket.connect ("tcp://127.0.0.1:5556")

# Subscribe to zipcode, default is NYC, 10001
zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"
socket.setsockopt(zmq.SUBSCRIBE, zip_filter)

# Process 5 updates

while True:
  total_temp = 0

  for update_nbr in range (5):
    print "waiting for image"
    string = socket.recv()
#    cv2.imshow("w2", string)
#    cv2.waitKey(10)
    zipcode, temperature, relhumidity = string.split()
    total_temp += int(temperature)

    print "Average temperature for zipcode '%s' was %dF" % (
          zip_filter, total_temp)
