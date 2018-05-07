from flask import request
from routes.main import MainRoute
from modules.led import Led


class Off(MainRoute):

    def __init__(self):
        super().__init__()

    def _generate_response(self, input_data=None):
        return super()._generate_response(input_data)

    def get(self):
        led = Led(8)
        led2 = Led(32)
        led.off()
        led2.off()
        return self._generate_response('Led turned off')
    
    def get_route(self):
        return '/off'