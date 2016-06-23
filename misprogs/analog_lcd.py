import mraa
import time
import pyupm_i2clcd as lcd
import pyupm_grove as grove
mylcd = lcd.Jhd1313m1(0, 0x3E,0x62)

mylcd.setCursor(0,0)
mylcd.setColor(0,0,255)
mylcd.write('Voltaje: ')
try:
	pinSensor=mraa.Aio(0)
	pinSensor.setBit(12)
	while True:
		valorSensor=pinSensor.read()
		mylcd.setCursor(1,0)
		mylcd.write("%.6f"%(valorsensor/819.0))
		time.sleep(1)
except:
	print "Seguro que tienes un ADC"
	mylcd.write("Seguro q conectaste")
