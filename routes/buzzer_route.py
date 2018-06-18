from routes.main import MainRoute
from modules.buzzer import Buzzer
from flask import request
import threading

class BuzzerRoute(MainRoute):
    def __init__(self):
        super().__init__()

    def _generate_response(self, input_data=None):
        return super()._generate_response(input_data)
    
    def get(self):
        buzzer = Buzzer(33)
        if buzzer.status():
            return self._generate_response('on')
        else:
            return self._generate_response('off')
    
    def post(self):
        def thread():
           buzzer = Buzzer(33)
           buzzer.play()
        
        act = request.form['action']
        t = threading.Thread(name='thread', target=thread)
        if act == 'on':
           t.start()
        else:
           t._stop()
        return self._generate_response(act)
    
    def get_route(self):
        return '/buzzer'