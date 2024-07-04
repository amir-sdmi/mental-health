from flask import jsonify
from werkzeug.exceptions import HTTPException

class ErrorHandler:
    @staticmethod
    #handle 400 error
    def handle_invalid_usage(error):
        response = {
            "error": "Invalid usage",
            "message": str(error),
        }
        return jsonify(response), 400

    @staticmethod
    #handle 404 error
    def handle_not_found(error):
        response = {
            "error": "Not found",
            "message": "The requested resource could not be found",
        }
        return jsonify(response), 404

    @staticmethod
    #handle 500 error
    def handle_internal_server_error(error):
        response = {
            "error": "Internal server error",
            "message": "An unexpected error occurred",
        }
        return jsonify(response), 500

    @staticmethod
    # create JSON response with the exception's name and description
    def handle_http_exception(error):
        response = {
            "error": error.name,
            "message": error.description,
        }
        return jsonify(response), error.code
# Initialize the error handlers
    @staticmethod
    def init_app(app):
        app.register_error_handler(400, ErrorHandler.handle_invalid_usage)
        app.register_error_handler(404, ErrorHandler.handle_not_found)
        app.register_error_handler(500, ErrorHandler.handle_internal_server_error)
        app.register_error_handler(HTTPException, ErrorHandler.handle_http_exception)