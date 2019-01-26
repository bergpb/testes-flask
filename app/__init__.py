from flask import Flask
from .todo import bp_todos

app = Flask(__name__)
app.register_blueprint(bp_todos, url_prefix='/api/v1')


@app.route('/')
def hello():
    return 'Hello World!'
