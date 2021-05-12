
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

User = get_user_model()


class StaticURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_about_author_url_exists_at_desired_location(self):
        """Проверка доступности адреса /about/author/."""
        response = self.guest_client.get('/about/author/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_about_tech_url_exists_at_desired_location(self):
        """Проверка доступности адреса /about/tech/."""
        response = self.guest_client.get('/about/tech/')
        self.assertEqual(response.status_code, HTTPStatus.OK)


class StaticViewsTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_about_author_page_accessible_by_name(self):
        """URL about:author доступен."""
        response = self.guest_client.get(reverse('about:author'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_about_tech_page_accessible_by_name(self):
        """URL about:tech доступен."""
        response = self.guest_client.get(reverse('about:tech'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_about_author_page_uses_correct_template(self):
        """При запросе к about:author
        применяется шаблон about/author.html."""
        response = self.guest_client.get(reverse('about:author'))
        self.assertTemplateUsed(response, 'about/author.html')

    def test_about_tech_page_uses_correct_template(self):
        """При запросе к about:tech
        применяется шаблон about/tech.html."""
        response = self.guest_client.get(reverse('about:author'))
        self.assertTemplateUsed(response, 'about/author.html')
