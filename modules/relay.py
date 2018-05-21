import RPi.GPIO as GPIO

class Relay(object):
    def __init__(self, pin_number):
        self.__pin = pin_number
        GPIO.setmode(GPIO.BOARD)
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
