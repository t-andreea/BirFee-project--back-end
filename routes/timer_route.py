from flask import request
from routes.main import MainRoute


class TimerRoute(MainRoute):

    def __init__(self):
        super().__init__()

    def _generate_response(self, input_data=None):
        return super()._generate_response(input_data)
    
    def get(self):
        var = open('time.txt','r')
        my_time = var.readline()
        var.close()
        return self._generate_response(my_time)

    def post(self):
        act = request.form['time']
        var = open('time.txt','w')
        var.write(act)
        var.close()
        return self._generate_response(act)
    
    def get_route(self):
        return '/timer'