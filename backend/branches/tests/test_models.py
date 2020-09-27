from django.test import TestCase
from branches.models import Branch


class TestModels(TestCase):

    def setUp(self):
        self.branch = Branch.objects.create(
            name='Moscow',
            facade='',
            latitude=56.239919,
            longitude=37.459023
        )

    def test_branch_to_json(self):
        result_json = dict(
            name=self.branch.name,
            facade=self.branch.facade,
            latitude=self.branch.latitude,
            longitude=self.branch.longitude
        )

        self.assertEqual(self.branch.to_json(), result_json)
