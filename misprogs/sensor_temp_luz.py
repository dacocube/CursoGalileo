import signal
import dweepy
import sys
import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd

def interruptHandler(signal, frame):
        sys.exit(0)
if __name__=='__main__':
        signal.signal(signal.SIGINT, interruptHandler)

        myLcd = lcd.Jhd1313m1(0, 0x3E,0x62)
	sensorluz=grove.GroveLight(0)
        sensortemperatura=grove.GroveTemp(1)

        coloR=0
        colorG=255
        colorB=0
        myLcd.setColor(coloR,colorG,colorB)

        #read the input and print, waiting 1/2 seconds between reading

        while True:
                valorSensor=sensortemperatura.value()
                myLcd.setCursor(0,0)
                myLcd.write('Temperatura: %2d'% valorSensor)
		valorSensor1=sensorluz.value()
		myLcd.setCursor(1,0)
                myLcd.write('Luz: %6d'% valorSensor1)
		datos = {"Temperatura":valorSensor, "Luz":valorSensor1}
		dweepy.dweet_for("dacocube",datos)
                time.sleep(0.5)

        del sensortemperatura
