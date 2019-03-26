from flask import Flask, render_template
from flask_cors import CORS
from domcek import api
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
    CORS(flask_app, resources={r"/api/*": {"origins": '*'}})
    return flask_app


def register_blueprints(flask_app):
    """Register Flask blueprints."""

    flask_app.register_blueprint(api.views.blueprint, url_prefix='/api')


app = create_app()


# Handler for vue app
@app.route("/", methods=['GET'])
def vue_app():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
      return render_template('index.html')

@app.errorhandler(500)
def server_error(error):
    return render_template('error.html'), 500
