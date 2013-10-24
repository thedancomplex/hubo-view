sudo ls > /dev/null
HUBO_VIEW_ROOT=$('pwd')
cd dep
tar -xvf zeromq-3.2.4.tar.gz
cd zeromq-3.2.4
./configure
make
sudo make install
cd $HUBO_VIEW_ROOT

# Python Dep
sudo apt-get install python-pip
sudo pip install ipython
sudo pip install --upgrade --user ipython
sudo easy_install ipython

# Python Bindings
sudo easy_install "pyzmq==2.0.10.1"
cd dep
tar -xvf pyzmq-13.0.2.tar.gz
cd pyzmq-13.0.2
sudo pip install cython
sudo python setup.py configure --zmq=/usr/local
sudo python setup.py configure --zmq=../zeromq-3.2.4
sudo python setup.py install 
pip install pyzmq --install-option="--zmq=bundled"


# Test python install
sudo python setup.py build_ext --inplace
python setup.py test
nosetests -vvs zmq.tests
