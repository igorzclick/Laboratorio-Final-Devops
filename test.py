import unittest
from app import app
import werkzeug

if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"items":["item1","item2","item3"]})

    def test_acesso_token(self):
        response_login = self.client.post('/login')
        token = response_login.json["access_token"]
        print(token)

        response_protected = self.client.get('/protected', headers={'Authorization': f"Bearer {token}"})
        self.assertEqual(response_protected.status_code, 200)
        self.assertEqual(response_protected.json, {'message': 'Protected route'})    


    def test_login_metodo_get(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()