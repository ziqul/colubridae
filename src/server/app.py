# External modules
from flask import Flask


def create_app(
    routes,
    error_handlers=None,
):
    app = Flask(__name__)
    for route in routes:
        app.add_url_rule(
            route,
            routes[route].__module__,
            routes[route])
    if error_handlers is not None:
        for error_code in error_handlers:
            app.register_error_handler(
                error_code,
                error_handlers[error_code])
    return app
