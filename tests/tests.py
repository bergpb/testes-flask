from unittest import TestCase, mock
from flask import url_for
from app import app


class RootTests(TestCase):
    def setUp(self):
        self.app = app
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def test_root_deve_retornar_hello_world(self):
        request = self.client.get(url_for('hello'))
        self.assertEqual('Hello World!', request.data.decode())


class TestTodo(TestCase):
    def setUp(self):
        self.app = app
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def test_root_deve_retornar_status_code_201(self):
        todo = 'dormir'
        request = self.client.post(url_for('todo.send_task', todo=todo))
        self.assertEqual(201, request.status_code)

    # mock para a lista todos no app
    @mock.patch('app.todo.todos')
    def test_put_deve_chamar_queue(self, m_queue):
        todo = 'dormir'
        self.client.post(url_for('todo.send_task', todo=todo))
        m_queue.append.assert_called()
