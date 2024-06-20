from flask import Flask, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)
names = {
    "tim":{"age":19 , "gender": "male"},}

class RequestHandler(Resource):
    def get(self,name):
        return names[name]

api.add_resource(RequestHandler, "/helloworld/<string:name>")



if __name__ == "__main__":
    app.run(debug=True)
