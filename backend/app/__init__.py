from flask import Flask
from flask_restful import Api
from app.resources.data_query import DataQuery
from app.error_handling import ErrorHandler

def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(DataQuery, "/data/<string:countryName>/<int:startDate>/<int:endDate>")

    # Initialize error handlers
    ErrorHandler.init_app(app)

    return app
