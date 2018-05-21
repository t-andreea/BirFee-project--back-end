from flask import request
from routes.main import MainRoute
from modules.sensor import Sensor


class SensorRoute(MainRoute):

    def __init__(self):
        super().__init__()

    def _generate_response(self, input_data=None):
        return super()._generate_response(input_data)

    def get(self):
        sensor = Sensor(14)
        ret = sensor.read()
        return self._generate_response(ret)
    
    def get_route(self):
        return '/sensor'
