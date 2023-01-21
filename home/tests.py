from django.test import TestCase, RequestFactory

from .views import HomeView


class TipInHomePageTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_null_tip_in_db(self):
        request = self.factory.get(path='/')
        home_view = HomeView.as_view()
        response = home_view(request)
        self.assertEqual(response.status_code, 200)
