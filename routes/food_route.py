from flask import request
from routes.main import MainRoute
from modules.relay import Relay
from modules.led import Led


class FoodRoute(MainRoute):

    def __init__(self):
        super().__init__()

    def _generate_response(self, input_data=None):
        return super()._generate_response(input_data)
    
    def get(self):
        rel = Relay.get_instance(10)
        if rel.status():
            return self._generate_response('on')
        else:
            return self._generate_response('off')

    def post(self):
        rel = Relay.get_instance(10)
        led = Led(19)
        act = request.form['action']
        if act=='on':
            rel.on()
            led.on()
        else:
            rel.off()
            led.off()
        return self._generate_response('The relay is ' + act)
    
    def get_route(self):
        return '/food'
