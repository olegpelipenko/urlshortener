from flask import Flask, request, jsonify, make_response, logging, g, current_app
import platform
from marshmallow import ValidationError
from functools import wraps
from typing import Dict
from appdirs import *

import os
import datetime
import logging
import atexit



def create_app():
    app_name = "urlshortener-api"
    app_author = "entrant"

    if platform.system() is 'Linux':
        app_dir = os.path.join('/opt/', app_name)
    else:
        app_dir = user_data_dir(app_name, app_author)
    logs_dir = os.path.join(app_dir, "logs")
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    print(logs_dir)

    logging.basicConfig(
        filename=os.path.join(logs_dir, "{}.log".format(datetime.datetime.now().isoformat(timespec='hours'))),
        filemode='a',
        level=logging.DEBUG,
        format='[%(asctime)s] %(process)d %(levelname)s %(module)s: %(message)s',
    )
    flask_app = Flask(__name__)
    return flask_app


app = create_app()


@app.route("/urls/", methods=['POST'])
def urls_create():
    return


@app.route("/urls/<string:short_code", methods=['GET'])
def urls_get():
    return


@app.route("/urls/<string:short_code>/stats", methods=['GET'])
def urls_stats():
    return


@app.route("/urls/<string:short_code>", methods=['PUT'])
def urls_put():
    return


@app.route("/urls/<string:short_code>", methods=['DELETE'])
def urls_delete():
    return


if __name__ == "__main__":
    port = 3000
    try:
        port = os.environ['APP_PORT']
    except Exception:
        pass

    app.run(host='0.0.0.0', port=port)
