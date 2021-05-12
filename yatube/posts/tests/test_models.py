import datetime as dt

from django.test import TestCase, Client
from django.contrib.auth.models import User

from ..models import Group, Post, Follow, Comment


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

    def test_follow_unfollow(self):
        """Авторизованный пользователь может подписываться на других пользователей
        и удалять их из подписок"""
        follow_before = Follow.objects.filter(user=self.user_1).count()
        self.assertEqual(follow_before, 0)
        Follow.objects.create(user=self.user_1, author=self.user_2)
        follow_after = Follow.objects.filter(user=self.user_1).count()
        self.assertEqual(follow_after, 1)
        Follow.objects.filter(user=self.user_1, author=self.user_2).delete()
        unfollow = Follow.objects.filter(user=self.user_1).count()
        self.assertEqual(unfollow, 0)


class CommentModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.post = Post.objects.create(
            text='Текст сообщения',
            pub_date=dt.date.today(),
            author=User.objects.create_user(username='user_1', ),
            group=Group.objects.create(
                title='Тестовое название группы',
                slug='test-slug',
                description='Тестовое описание группы',
            )
        )

        cls.user_2 = User.objects.create(username='user_2')

    def setUp(self):
        self.authorized_client_1 = Client()
        self.authorized_client_1.force_login(self.post.author)

        self.authorized_client_2 = Client()
        self.authorized_client_2.force_login(self.user_2)

        self.guest_client = Client()

    def test_create_comments(self):
        """Авторизированный пользователь может
        оставлять комментарии"""
        comments_before = Comment.objects.filter(author=self.user_2).count()
        self.assertEqual(comments_before, 0)
        Comment.objects.create(
            post=self.post,
            author=self.user_2,
            text='Комментарий')
        comments_after = Comment.objects.filter(author=self.user_2).count()
        self.assertEqual(comments_after, 1)
