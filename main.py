# import RPi.GPIO as GPIO
import threading
from flask import Flask
from routes.sensor_route import SensorRoute
from routes.water_route import WaterRoute
from routes.food_route import FoodRoute
from routes.buzzer_route import BuzzerRoute
from modules.relay import Relay
from modules.led import Led
from modules.button import Button
from modules.buzzer import Buzzer

buzzer = Buzzer(33)

def sound():
    buzzer.play()

t2 = threading.Thread(name='sound', target=sound)

def manual():
    led = Led(37)
    fled = Led(19)
    wled = Led(38)
    button = Button(11)
    food = Relay.get_instance(10)
    water = Relay.get_instance(12)
    
    while True:
        value = button.multi_checked(led)
        if value == 1:
           water.off()
           wled.off()
           food.off()
           fled.off()
           buzzer.stop()
        if value == 2:
           wled.on()
           water.on()
        if value == 3:
           fled.on()
           food.on()
        if value == 4:
           t2.start()
           

def api():
    app = Flask(__name__)

    routes = [
        SensorRoute(),
	WaterRoute(),
        FoodRoute(),
        BuzzerRoute()
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