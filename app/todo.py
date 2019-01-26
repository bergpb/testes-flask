from flask import Blueprint, jsonify

todos = []

bp_todos = Blueprint('todo', __name__)


@bp_todos.route('/task/<string:todo>', methods=['POST'])
def send_task(todo):
    todos.append(todo)
    return jsonify('ok'), 201
