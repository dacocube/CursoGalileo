import signal
import sys
import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd
def interruptHandler(signal, frame):
        sys.exit(0)
if __name__=='__main__':
        signal.signal(signal.SIGINT, interruptHandler)

        myLcd = lcd.Jhd1313m1(0, 0x3E,0x62)
        sensortemperatura=grove.GroveTemp(1)

        coloR=255
        colorG=200
        colorB=100
        myLcd.setColor(coloR,colorG,colorB)

        #read the input and print, waiting 1/2 seconds between reading

        while True:
                valorSensor=sensortemperatura.value()
                myLcd.setCursor(0,0)
                myLcd.write('%6d'% valorSensor)
                time.sleep(0.5)

        del sensortemperatura

