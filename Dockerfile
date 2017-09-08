FROM keyi/python2-mcr2017a-rpi-isl

COPY JSTMB_O38/ ./JSTMB_O38
COPY setup.py ./
COPY O38_JSTMB_wrapper.py ./
COPY trainData.csv ./
COPY trainTargets.csv ./
