from modules.led import Led
from modules.button import Button

led = Led(8)
led2 = Led(32)
button = Button(36)
try:
    while True:
        if button.check():
            if led.status():
                led.off()
                led2.on()
            else:
                led.on()
                led2.off()
#led.off()            
except KeyboardInterrupt:
    import RPi.GPIO as GPIO
    GPIO.cleanup()

