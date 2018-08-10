from flask import Flask
from flask_restful import Api
from rainbowcontroller import RainbowController

application = Flask(__name__)
api = Api(application)

api.add_resource(RainbowController, '/')

if __name__ == '__main__':
    application.run()
