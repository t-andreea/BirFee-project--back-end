from flask import request
from routes.main import MainRoute
from modules.relay import Relay
from modules.led import Led


class WaterRoute(MainRoute):

    def __init__(self):
        super().__init__()

    def _generate_response(self, input_data=None):
        return super()._generate_response(input_data)
    
    def get(self):
        rel = Relay.get_instance(12)
        if rel.status():
            return self._generate_response('on')
        else:
            return self._generate_response('off')

    def post(self):
        rel = Relay.get_instance(12)
        led = Led(38)
        act = request.form['action']
        if act=='on':
            rel.on()
            led.on()
        else:
            rel.off()
            led.off()
        return self._generate_response(act)
    
    def get_route(self):
        return '/water'