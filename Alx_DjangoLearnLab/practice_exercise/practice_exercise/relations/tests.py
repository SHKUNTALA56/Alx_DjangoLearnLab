from django.test import TestCase
from django.urls import reverse

class ViewsTestCase(TestCase):
    def test_current_datetime(self):
        response = self.client.get(reverse('current_datetime'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('It is now', response.content.decode())