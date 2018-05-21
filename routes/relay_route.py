from flask import request
from routes.main import MainRoute
from modules.relay import Relay

class RelayRoute(MainRoute):

    def __init__(self):
        super().__init__()

    def _generate_response(self, input_data=None):
        return super()._generate_response(input_data)
    
    def post(self):
        rel = Relay(12)
        act = request.form['action']
        if act=='on':
            rel.on()
        else:
            rel.off()
        return self._generate_response('The reay is ' + act)
    
    def get_route(self):
        return '/water'