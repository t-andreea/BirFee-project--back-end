import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class Button(object):
    def __init__(self, pin_number):
        self.__pin = pin_number
        GPIO.setup(self.__pin, GPIO.IN)

    def check(self):
        __button_pressed = GPIO.input(self.__pin)
        if __button_pressed == True:
            return True
        return False

    def __del__(self):
        pass

    
