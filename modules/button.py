import time
import RPi.GPIO as GPIO
from modules.led import Led
GPIO.setmode(GPIO.BOARD)

class Button(object):
    def __init__(self, pin_number):
        self.__pin = pin_number
        GPIO.setup(self.__pin, GPIO.IN)

    def check(self):
        __button_pressed = GPIO.input(self.__pin)
        if __button_pressed:
            return True
        return False
    
    def multi_checked(self, led_obj):
        t = time.time()
        c = 0
        led = led_obj
        while time.time()-t < 2:
            if self.check():
               led.on()
               while self.check():
                   pass
               c+=1
               t = time.time()
               led.off()
               time.sleep(0.1)
        return c
        
    def __del__(self):
        pass

    
