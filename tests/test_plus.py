from decimal import Decimal
import unittest

from app import app


class PlusTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_sum_integers(self):
        response = self.app.get('/plus/3/5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'result': 8})

    def test_sum_floats(self):
        response = self.app.get('/plus/2.5/3.5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'result': Decimal('6.0')})

    def test_sum_float_and_integer(self):
        response = self.app.get('/plus/4.0/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'result': 8})

    def test_invalid_input(self):
        response = self.app.get('/plus/abc/2')
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            'Invalid input: both parameters must be numbers',
            response.data.decode()
        )

    def test_large_floats(self):
        response = self.app.get('/plus/1.1111111111111111/2.2222222222222222')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'result': 3.3333333333333335})


if __name__ == "__main__":
    unittest.main()
