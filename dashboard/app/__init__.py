from flask import Flask
from . import print_data
import os
import config

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('../config.py', silent=False)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.register_blueprint(print_data.bp)
    # app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app
