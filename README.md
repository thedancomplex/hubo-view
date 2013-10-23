hubo-view
=========

a common framework for streaming sensor data (vision, depth, forces, encoders) to a remote terminal

The terminal should have a *nice* visualization of this data built on top of RVIZ.  This framework, let’s call it “HuboView”, should be usable for all tasks.  It should also handle bandwidth limitations by throttling the rate of data transfer.

Prerequisits:
ZeroMQ (3.2.4): http://zeromq.org/
wget: http://download.zeromq.org/zeromq-3.2.4.tar.gz
