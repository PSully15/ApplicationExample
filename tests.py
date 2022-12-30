from app import app
from unittest import TestCase

app.config['WTF_CSRF_ENABLED'] = False


class SnackViewsTestCases(TestCase):
    """Tests for views for Snacks."""

    def test_snack_add_form(self):
        with app.test_client() as client:
            resp = client.get("/add")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form id="snack_id_form', html)

    
    def test_snack_add(self):
        with app.test_client() as client:
            d = {"name": 'Test2', "price": 2}
            resp = client.post("/add", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("added Test2 at 2", html)