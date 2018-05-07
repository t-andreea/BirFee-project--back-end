from flask import request
from routes.main import MainRoute
from modules.led import Led
import time


class On(MainRoute):

    def __init__(self):
        super().__init__()

    def _generate_response(self, input_data=None):
        return super()._generate_response(input_data)

    def get(self):
        led = Led(8)
        led2 = Led(32)
        led.on()
        led2.on()
        return self._generate_response('Led turned on')
    
    def get_route(self):
        return '/on'