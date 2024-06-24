from flask import Flask
from flask_restful import Api
from Request_handler import DataQuery

app = Flask(__name__)
api = Api(app)

api.add_resource(DataQuery, "/data/<string:countryName>/<int:startDate>/<int:endDate>")

if __name__ == "__main__":
    app.run(debug=True)
