from modules.led import Led
from modules.button import Button
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

led = Led(37)
button = Button(11)

while True:
    print(button.check())