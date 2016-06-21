#!/usr/bin/python
import time
import sys
import signal
def manejadorsenial(signal, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, manejadorsenial)
while (True):
    print "Hola, desde el curso de Intel Galileo"
    time.sleep(5)
#Fin de archivo

