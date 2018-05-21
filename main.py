from flask import Flask

from routes.sensor_route import SensorRoute
from routes.relay_route import RelayRoute

from modules.led import Led
from modules.button import Button

def manual():
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

    except KeyboardInterrupt:
        import RPi.GPIO as GPIO
        GPIO.cleanup()
    
def api():
    app = Flask(__name__)

    routes = [
        SensorRoute(),
	RelayRoute()
    ]

    for route in routes:
        app.add_url_rule(route.get_route(), view_func=route.as_view(route.get_route()))
    
    app.run(host='0.0.0.0', debug=True)

api()