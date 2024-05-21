import unittest
from random_post_generator import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_random_pattern(self):
        response = self.app.get('/random-pattern')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')


if __name__ == '__main__':
    unittest.main()
