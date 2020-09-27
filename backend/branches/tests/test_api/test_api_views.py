import json
from rest_framework.test import APITestCase
from branches.models import Branch


class TestAPI(APITestCase):

    def setUp(self):
        self.api_prefix = '/api/branches/'
        self.branch = Branch.objects.create(
            name='Moscow',
            facade='',
            latitude=55.8,
            longitude=37.5
        )

    def test_branch_get(self):
        response = self.client.get(f'{self.api_prefix}branch/')
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(content), 1)
        self.assertEqual(content[0].get('name'), 'Moscow')

    def test_particular_branch_get(self):
        response = self.client.get(f'{self.api_prefix}branch/{self.branch.id}/')
        self.assertEqual(response.status_code, 200)

    def test_branch_post(self):
        post_response = self.client.post(f'{self.api_prefix}branch/', data=dict(
            name='Belgrade',
            facade='',
            latitude=44.8,
            longitude=20.4
        ))
        self.assertEqual(post_response.status_code, 201)
        get_response = self.client.get(f'{self.api_prefix}branch/')
        content = json.loads(get_response.content)
        self.assertEqual(len(content), 2)
        self.assertEqual('Belgrade', content[1].get('name'))

    def test_branch_del(self):
        del_response = self.client.delete(f'{self.api_prefix}branch/{self.branch.id}/')
        self.assertEqual(del_response.status_code, 204)
        get_response = self.client.get(f'{self.api_prefix}branch/{self.branch.id}/')
        self.assertEqual(get_response.status_code, 404)

    def test_branch_put(self):
        put_response = self.client.put(f'{self.api_prefix}branch/{self.branch.id}/', data=dict(
            name='Belgrade',
            facade='',
            latitude=44.8,
            longitude=20.4
        ))
        self.assertEqual(put_response.status_code, 200)
        get_response = self.client.get(f'{self.api_prefix}branch/')
        content = json.loads(get_response.content)
        self.assertEqual(len(content), 1)
        self.assertEqual('Belgrade', content[0].get('name'))
