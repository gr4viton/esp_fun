import dht
import machine
from time import sleep 

class TempSensor():
    def __init__(self):
    	self.sensor= dht.DHT22(machine.Pin(14))

    def sample(self, log=False):
	d = self.sensor.measure()
	temp = self.sensor.temperature()
	hum = self.sensor.humidity()
	if log:
	    print('temp {}'.format(temp))
	    print('hum {}'.format(hum))
	    print('-'*10)
	sleep(2)
	return temp, hum

