from django.test import TestCase, Client
from django.contrib.auth.models import User

from ..models import Group, Post


class GroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.group = Group.objects.create(
            title='Тестовое название группы',
            slug='test-slug',
            description='Тестовое описание группы'
        )

    def test_str_equals_title(self):
        """Проверка совпадения значения поля __str__ с полем title"""
        group_test = GroupModelTest.group
        title = group_test.title
        self.assertEqual(str(group_test), title)


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.post = Post.objects.create(
            text='Тестовое сообщение поста',
            author=User.objects.create(username='test_user'),
        )

    def test_str_equals_text(self):
        post_test = PostModelTest.post
        text = post_test.text
        self.assertEqual(str(post_test), text[:15])


class FollowModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user_1 = User.objects.create(username='user_1')
        cls.user_2 = User.objects.create(username='user_2')

    def setUp(self):
        self.authorized_client_1 = Client()
        self.authorized_client_1.force_login(self.user_1)

        self.authorized_client_2 = Client()
        self.authorized_client_2.force_login(self.user_2)
