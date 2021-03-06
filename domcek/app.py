import sys
from os import path
from datetime import datetime
from flask import Flask, render_template, redirect
from flask_cors import CORS
from domcek import sync
from domcek import offline
from domcek.settings import ProdConfig


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    if getattr(sys, 'frozen', False):
        template_folder = path.join(sys._MEIPASS, 'templates')
        static_folder = path.join(sys._MEIPASS, 'static')
        flask_app = Flask(__name__.split('.')[0], template_folder=template_folder, static_folder=static_folder)
    else:
        flask_app = Flask(__name__.split('.')[0])

    flask_app.url_map.strict_slashes = False
    flask_app.config.from_object(config_object)
    register_blueprints(flask_app)
    CORS(flask_app, resources={r"/sync/*": {"origins": '*'}})
    return flask_app


def register_blueprints(flask_app):
    """Register Flask blueprints."""

    flask_app.register_blueprint(offline.views.blueprint, url_prefix='/registration')
    flask_app.register_blueprint(sync.views.blueprint, url_prefix='/sync')


app = create_app()


# Handler for vue app
@app.route("/", methods=['GET'])
def index():
    return redirect('/registration')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')


@app.errorhandler(500)
def server_error(error):
    return render_template('error.html'), 500


@app.template_filter('year_is_more')
def year_is_more_filter(d, years):
    now = datetime.now()
    year = now.year - years

    result = datetime.strptime(d, '%Y-%m-%d')
    return result.year > year


@app.template_filter('bus')
def year_is_more_filter(text):
    return True if text and type(text) is str and ':' in text else False

