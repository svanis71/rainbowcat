from flask_restful import Resource

class RainbowController(Resource):
    def get(self):
        return 'Hello rainbow!', 200
    
