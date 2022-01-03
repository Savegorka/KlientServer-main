from ..common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from ..client import create_presence, answer
import unittest


class TestClass(unittest.TestCase):
    def test_def_presense(self):
        """Тест коректного запроса"""
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """Тест корректного разбора ответа 200"""
        self.assertEqual(answer({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        """Тест корректного разбора 400"""
        self.assertEqual(answer({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, answer, {ERROR: 'Bad Request'})

#  Не понял, нужно ли тестировать main
