import os
from bottle import default_app, route, run, redirect


@route('/')
def hello_world():
    return "Hello from Bottle!"

@route('/public')
def get_public():
    return "This public message should be shown to everyone!"


@route('/secret')
def get_secret():
    return "This secret message should only be shown to authorized people"

@route('/login')
def get_login():
    return "OK - looks like you've logged in"

if'PYTHONANYWHERE_DOMAIN' in os.environ:
    application = default_app()
else:
    run(host='localhost', port=8080)