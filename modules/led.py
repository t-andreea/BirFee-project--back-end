import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class Led(object):
    def __init__(self, pin_number):
        self.__pin = pin_number
        GPIO.setup(self.__pin, GPIO.OUT)
        self.__status = False

    def on(self):
        GPIO.output(self.__pin, GPIO.HIGH)
        self.__status = True

    def off(self):
        GPIO.output(self.__pin, GPIO.LOW)
        self.__status = False

    def status(self):
        return self.__status
    
    def __del__(self):
        #self.off()
        pass
