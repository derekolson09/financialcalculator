from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        # Default to 200 OK
        return({'hello':'world'})

api.add_resource(Test, '/')