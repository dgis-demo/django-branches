from django.test import TestCase
from branches import forms


class TestForms(TestCase):

    def test_branch_form_is_valid(self):
        form = forms.BranchForm(data={
            'name': 'Moscow',
            'facade': '',
            'latitude': -89.999999,
            'longitude': 179.999999
        })

        self.assertTrue(form.is_valid())

    def test_branch_form_is_not_valid(self):
        latitude = [
            90, 91, -90, -91, 89.000001, 89.0000001
        ]
        longitude = [
            181, 180, -181, -180, 179.0000001, 179.000001
        ]
        test_coordinates = zip(latitude, longitude)

        for coord in test_coordinates:

            form = forms.BranchForm(data={
                'name': 'Moscow',
                'facade': '',
                'latitude': coord[0],
                'longitude': coord[1]
            })

            self.assertFalse(form.is_valid())
