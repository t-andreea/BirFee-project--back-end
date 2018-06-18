# import RPi.GPIO as GPIO
import threading
import datetime
import time

from flask import Flask
from routes.sensor_route import SensorRoute
from routes.water_route import WaterRoute
from routes.food_route import FoodRoute
from routes.buzzer_route import BuzzerRoute
from routes.timer_route import TimerRoute
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
           
def automatic_feeder():
    led = Led(37)
    fled = Led(19)
    wled = Led(38)
    food = Relay.get_instance(10)
    water = Relay.get_instance(12)
    
    def read_from_file():
        var = open('time.txt','r')
        my_time = var.readline()
        var.close()
        return my_time
    
    while True:
        now = datetime.datetime.now()
        
        if str(now.hour) + ':' + str(now.minute) == str(read_from_file()):
           fled.on()
           food.on()
           wled.on()
           water.on()
           time.sleep(5)
           water.off()
           wled.off()
           time.sleep(10)
           food.off()
           fled.off()
           
        time.sleep(30)
        

def api():
    app = Flask(__name__)

    routes = [
        SensorRoute(),
	WaterRoute(),
        FoodRoute(),
        BuzzerRoute(),
        TimerRoute()
    ]

    for route in routes:
        app.add_url_rule(route.get_route(), view_func=route.as_view(route.get_route()))
    
    app.run(host='0.0.0.0')

# GPIO.cleanup()
# api()

t = threading.Thread(name='manual', target=manual)
t1 = threading.Thread(name='api', target=api)
t3 = threading.Thread(name='automatic_feeder', target=automatic_feeder)

t.start()
t1.start()
t3.start()


try:
   t.join()
   t1.join()
   t3.join()
   
except KeyboardInterrupt:
   import RPi.GPIO as GPIO
   GPIO.cleanup()