from flask import Flask, request, make_response, jsonify, logging
from functools import wraps
from appdirs import *
from marshmallow import ValidationError

import string, os, json, random

import cache, stats


urls_cache = {}
host_name = 'http://urlshortener.sh'

def create_app():
    flask_app = Flask(__name__)
    return flask_app

app = create_app()


def response_wrap(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)

        except ValidationError as e:
            app.logger.error(e.messages)
            return make_response(jsonify({'error': e.messages}), 400)

        except Exception as e:
            app.logger.error(e)
            return make_response(jsonify({'error': e.args}), 500)

    return wrapper


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    #return 'aaa'


def get_long_url():
    json_data = request.get_json()
    if "long_url" not in json_data:
        raise ValidationError(message="no input data provided")

    return json_data["long_url"]


@app.route("/urls/", methods=['POST'])
@response_wrap
def urls_create():
    long_url = get_long_url()

    short_code = id_generator()
    cache.store_short_url(short_code, long_url)
    
    return make_response(
        "{}/urls/{}".format(host_name, short_code), 
        200
    )


@app.route("/urls/<short_code>", methods=['GET'])
@response_wrap
def urls_get(short_code):
    if cache.is_short_code_exists(short_code):
        raise ValidationError(message="bad short_code")
    
    stats.make_visit(short_code)

    return make_response(cache.get_long_url[short_code], 200)


@app.route("/urls/<short_code>/stats", methods=['GET'])
@response_wrap
def urls_stats(short_code):
    return make_response(
        json.dumps({'visits': stats.get_stats(short_code),}),
        200
    )


@app.route("/urls/<short_code>", methods=['PUT'])
@response_wrap
def urls_put(short_code):
    if cache.is_short_code_exists(short_code):
        raise ValidationError(message="bad short_code")

    long_url = get_long_url()
    cache.store_short_url(short_code, long_url)

    return make_response('', 200)


@app.route("/urls/<short_code>", methods=['DELETE'])
@response_wrap
def urls_delete(short_code):
    if short_code not in urls_cache:
        raise ValidationError(message="bad short_code")

    cache.remove_short_code(short_code)
    stats.cleanup_visits(short_code)

    return make_response('', 200)


if __name__ == "__main__":
    port = 3000
    try:
        port = os.environ['APP_PORT']
    except Exception:
        pass

    app.run(host='0.0.0.0', port=port)
