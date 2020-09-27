from django.test import TestCase
from django.urls import reverse, resolve
from branches import views


class TestUrls(TestCase):

    def test_index(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, views.index_view)
