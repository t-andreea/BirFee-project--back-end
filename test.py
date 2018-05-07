from led import Led
from button import Button

led = Led(8)
button = Button(36)

while True:
    if button.check():
        if led.status():
            led.off()
        else:
            led.on()
#led.off()

