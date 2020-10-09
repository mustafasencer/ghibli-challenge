from os import environ

from flask import Flask, render_template
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_redis import FlaskRedis

from utils.error import AppError


def init_error_handler(app):
    @app.errorhandler(AppError)
    def handle_app_error(e):
        return render_template('list_films.html', exception=True), 400

    @app.errorhandler(404)
    def not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(429)
    def too_many_requests(e):
        return render_template("429.html"), 429

    @app.errorhandler(Exception)
    def handle_exception(e):
        return render_template("500.html"), 500


def init_extensions(app):
    CORS(app)
    limiter.init_app(app)
    redis_client.init_app(app)


def register_blueprints(app):
    from app import index
    from app import movies
    app.register_blueprint(index.bp)
    app.register_blueprint(movies.bp)


limiter = Limiter(key_func=get_remote_address, default_limits=["30 per minute"])
redis_client = FlaskRedis()


def create_app():
    app = Flask(__name__, static_url_path='/static', static_folder='../static', template_folder='../templates')
    app.config['GHIBLI_URL'] = environ.get("GHIBLI_URL")
    app.config['REDIS_URL'] = environ.get('REDIS_URL')
    init_error_handler(app)
    init_extensions(app)
    register_blueprints(app)
    return app
