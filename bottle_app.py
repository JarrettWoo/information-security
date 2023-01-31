import os
from bottle import default_app, route


@route('/')
def hello_world():
    return "Hello from Bottle!"

@route('/public')
def hello_world():
    return "This public message should be shown to everyone!"


@route('/secret')
def hello_world():
    return "This secret message should only be shown to authorized people"



if'PYTHONANYWHERE_DOMAIN' in os.environ:
    application = default_app()
else:
    run(host='localhost', port=8080)