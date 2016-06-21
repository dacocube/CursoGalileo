import mraa
import time
try:
	pinSensor=mraa.Aio(0)
	pinSensor.setBit(12)
	while True:
		valorSensor=pinSensor.read()
		print "%.6f" %(valorSensor/819.0)
		time.sleep(1)
except:
	print "Seguro que tienes un ADC"

