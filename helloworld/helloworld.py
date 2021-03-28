import os
import socket

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Greeting(Resource):
    def get(self):
        return {
            "version": os.getenv("VERSION", "undefined"),
            "greeting": os.getenv("GREETING", "Hello"),
            "hostname": socket.gethostname(),
        }


class Env(Resource):
    # WARNING: This exposes all environements, please be careful with your sensitive information
    def get(self):
        return {k: v for k, v in os.environ.items()}


api.add_resource(Greeting, '/')
api.add_resource(Env, '/envs')

if __name__ == '__main__':
    app.run('0.0.0.0','8080')

