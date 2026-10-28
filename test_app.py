import unittest
from app import app


class AppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

    def test_hello(self):
        response = self.client.get("/hello/Selma")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Selma", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()