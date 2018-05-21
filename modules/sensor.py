import RPi.GPIO as GPIO
import Adafruit_DHT

class Sensor:
    def __init__(self, BCM_pin):
        ''' You have to use the BCM pin '''
        self.pin = BCM_pin

    def read(self):
        humidity, temperature = Adafruit_DHT.read_retry(11, self.pin)
        return_value = dict()
        return_value['humidity'] = humidity
        return_value['temperature'] = temperature
        return return_value

