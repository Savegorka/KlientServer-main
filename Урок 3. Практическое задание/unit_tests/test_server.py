from ..common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from ..server import process_client_message
import unittest


class TestServer(unittest.TestCase):
    err_dict = {
        RESPONSE: 200,
        ERROR: 'Value Error'
    }
    ok_dict = {RESPONSE: 200}

    def test_no_action(self):
        """Ошибка если нет действия"""
        self.assertEqual(process_client_message(
            {TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_no_user(self):
        """Ошибка - нет пользователя"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: '1.1'}), self.err_dict)

    def test_unknown_user(self):
        """Ошибка - не Guest"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}), self.err_dict)

    def test_ok_check(self):
        """Корректный запрос"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)
