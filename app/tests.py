from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from app.models import User, Status


class TestLoginAndRegistration(TestCase):
    def test_login(self):
        User.objects.create_user(username='admin', password='admin')
        client = Client()
        response = client.post(
            path=reverse('login'), data={'username': "admin", "password": "admin"}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_registration(self):
        client = Client()
        response = client.post(
            path=reverse('register'), data={'username': "admin",
                                            "first_name": "john",
                                            "last_name": "connor",
                                            "password1": "admin",
                                            "password2": "admin"}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username='admin')
        self.assertTrue(user)
        self.assertEqual(user.first_name, 'john')
        self.assertEqual(user.last_name, 'connor')


class TestStatusCRUD(TestCase):
    def test_create_status(self):
        user = User.objects.create_user(username='admin', password='admin')
        client = Client()
        client.force_login(user)
        response = client.post(
            path=reverse('create_stat'), data={'name': "admin"}, follow=True)
        self.assertEqual(response.status_code, 200)
        status = Status.objects.get(name='admin')
        self.assertTrue(status)
        self.assertEqual(status.name, 'admin')

    def test_update_status(self):
        user = User.objects.create_user(username='admin', password='admin')
        client = Client()
        client.force_login(user)
        status = Status.objects.create(name='old_status')
        response = client.post(
            path=reverse(
                'update_stat',
                args=[str(status.pk)]),
            data={'name': "admin"}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        status = Status.objects.get(name='admin')
        self.assertTrue(status)
        self.assertEqual(status.name, 'admin')

    def test_delete_status(self):
        user = User.objects.create_user(username='admin', password='admin')
        client = Client()
        client.force_login(user)
        status = Status.objects.create(name='old_status')
        response = client.post(
            path=reverse(
                'delete_stat',
                args=[str(status.pk)]), follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Status.objects.all()), 0)

