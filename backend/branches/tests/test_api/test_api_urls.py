from django.test import TestCase
from django.urls import reverse, resolve
from branches.api import views


class TestApiUrls(TestCase):

    def test_closest_branch(self):
        url = reverse('closest_branch')
        self.assertEqual(resolve(url).func, views.closest_branch)
