import json
import logging
import os
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from werkzeug.local import LocalProxy


from bard_api.api import api

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.WARN)
    CORS(
        app,
        supports_credentials=True,
        origins=[
            "http://localhost:3000"
        ]
    )
    app.config.from_object('bard_api.config')
    if os.getenv('BARDAPI_SETTINGS'):
        app.config.from_envvar('BARDAPI_SETTINGS')
    app.register_blueprint(api)
    return app