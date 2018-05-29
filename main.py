# import RPi.GPIO as GPIO
import threading
from flask import Flask
from routes.sensor_route import SensorRoute
from routes.relay_route import RelayRoute
from modules.relay import Relay
from modules.led import Led
from modules.button import Button


def manual():
    led = Led(36)
    button = Button(37)
    rel = Relay.get_instance(12)
    while True:
        value = button.multi_checked(Led(7))
        if value == 1:
           rel.off()
        if value == 2:
           pass
        if value == 3:
           rel.on()
        if value == 4:
           pass


def api():
    app = Flask(__name__)

    routes = [
        SensorRoute(),
	RelayRoute()
    ]

    for route in routes:
        app.add_url_rule(route.get_route(), view_func=route.as_view(route.get_route()))
    
    app.run(host='0.0.0.0')

# GPIO.cleanup()
# api()

t = threading.Thread(name='manual', target=manual)
t1 = threading.Thread(name='api', target=api)

t.start()
t1.start()

try:
   t.join()
   t1.join()
except KeyboardInterrupt:
   import RPi.GPIO as GPIO
   GPIO.cleanup()