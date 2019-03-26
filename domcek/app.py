from flask import Flask, render_template
from domcek import registration
from domcek.settings import ProdConfig


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    flask_app = Flask(__name__.split('.')[0])
    flask_app.url_map.strict_slashes = False
    flask_app.config.from_object(config_object)
    register_blueprints(flask_app)
    return flask_app


def register_blueprints(flask_app):
    """Register Flask blueprints."""

    flask_app.register_blueprint(registration.views.blueprint)


app = create_app()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.errorhandler(500)
def page_not_found(error):
    return render_template('error.html'), 500
