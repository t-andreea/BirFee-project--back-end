from routes.main import MainRoute
from modules.buzzer import Buzzer

class BuzzerRoute(MainRoute):
    def __init__(self):
        super().__init__()

    def _generate_response(self, input_data=None):
        return super()._generate_response(input_data)
    
    def post(self):
        buzzer = Buzzer(32)
        act = request.form['action']
        if act == 'start':
           buzzer.play()
        else:
           buzzer.stop()
    
    def get_route(self):
        return '/buzzer'