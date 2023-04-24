from django.test import TestCase, RequestFactory

from .views import HomeView
from .helpers import get_jar_info, get_donate_jar_box_info


class TipInHomePageTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_null_tip_in_db(self):
        request = self.factory.get(path='/')
        home_view = HomeView.as_view()
        response = home_view(request)
        self.assertEqual(response.status_code, 200)


class DonateJarBoxInHomePageTestCase(TestCase):

    def test_jar_info_is_none(self):
        self.assertIsNot(get_jar_info(), None)

    def test_donate_jar_box(self):
        donate_jar_box = get_donate_jar_box_info()
