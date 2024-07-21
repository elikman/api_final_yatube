from django.test import TestCase, Client
from .models import Group


class GroupTestCase(TestCase):
    def test_create_group(self):
        client = Client()
        response = client.post('/api/v1/groups/', {'title': 'Test Group'})
        self.assertEqual(response.status_code, 201)
        group = Group.objects.get(title='Test Group')
        self.assertIsNotNone(group)

    def test_retrieve_group(self):
        group = Group.objects.create(title='Test Group')
        client = Client()
        response = client.get(f'/api/v1/groups/{group.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Group')
