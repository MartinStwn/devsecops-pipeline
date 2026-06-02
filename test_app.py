import unittest
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Set up test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Test the home page
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello', response.data)  # Sesuaikan dengan output di app.py

if __name__ == "__main__":
    unittest.main()
