import unittest
import json
from ..common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from ..common.utils import get_message, send_message

class TestSocket:
    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.recieved_message = None

    def send(self, message_to_send):
        json_test_message = json.dumps(self.test_dict)
        # кодирует сообщение
        self.encoded_message = json_test_message.encode('utf-8')
        # сохраняем что должно было отправлено в сокет
        self.recieved_message = message_to_send

    def receive(self):
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode('utf-8')


class Tests(unittest.TestCase):
    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 222222.222222,
        USER: {
            ACCOUNT_NAME: 'tested_tested'
        }
    }
    test_dict_recieve_ok = {RESPONSE: 200}
    test_dict_recieve_error = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    def test_send_message(self):
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertEqual(test_socket.encoded_message, test_socket.recieved_message)
        with self.assertRaises(Exception):
            send_message(test_socket, test_socket)

    def test_get_message(self):
        test_sock_ok = TestSocket(self.test_dict_recieve_ok)
        test_sock_err = TestSocket(self.test_dict_recieve_error)
        self.assertEqual(get_message(test_sock_ok), self.test_dict_recieve_ok)
        self.assertEqual(get_message(test_sock_err), self.test_dict_recieve_error)
