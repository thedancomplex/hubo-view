hubo-view
=========

a common framework for streaming sensor data (vision, depth, forces, encoders) to a remote terminal

The terminal should have a *nice* visualization of this data built on top of RVIZ.  This framework, let’s call it “HuboView”, should be usable for all tasks.  It should also handle bandwidth limitations by throttling the rate of data transfer.

Prerequisits:
Ach
OpenCV2

Install:
./hubo-view install

Usage:
---- Hubo-View arg list ----
client        : starts client (reads from server)
server        : starts server
remote        : Starts a remote connection to xxx.xxx.xxx.xxx via achd
              : can put at end of any other command. 
              : if client will pull (default) to IP, if server will push
              : Options:
                     xxx.xxx.xxx.xxx      : sets connection to IP xxx.xxx.xxx.xxx
                     kill                 : kills remote connections
install       : Installs hubo-view to /etc/hubo/hubo-view
remove        : Removes hubo-view
kill          : Kills and removes hubo-view and ach channels
make          : makes ach channels
