import datetime as dt
import shutil
import tempfile

from django import forms
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from posts.forms import PostForm, CommentForm
from ..models import Group, Post, Follow, Comment

User = get_user_model()


class ViewsPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        settings.MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)

        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x02\x00'
            b'\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
            b'\x00\x00\x00\x2C\x00\x00\x00\x00'
            b'\x02\x00\x01\x00\x00\x02\x02\x0C'
            b'\x0A\x00\x3B'
        )

        uploaded = SimpleUploadedFile(
            name='small.gif',
            content=small_gif,
            content_type='image/gif'
        )

        cls.empty_group = Group.objects.create(
            title='Название группы_2',
            description='Описание группы_2',
            slug='test_slug_2'
        )

        cls.post = Post.objects.create(
            text='Текст сообщения',
            pub_date=dt.date.today(),
            author=User.objects.create_user(username='test_user', ),
            image=uploaded,
            group=Group.objects.create(
                title='Тестовое название группы',
                slug='test-slug',
                description='Тестовое описание группы',
            )
        )

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.post.author)

    def test_pages_use_correct_template(self):
        """URL-адрес использует соответствующий шаблон"""
        templates_pages_names = {
            'index.html': reverse('index'),
            'group.html': reverse(
                'group', kwargs={'slug': self.post.group.slug}),
            'new_post.html': reverse('new_post'),
            # Добавил проверку шаблона follow.html
            'follow.html': reverse('follow_index')
        }

        for template, reverse_name in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template)

    def test_index_correct_context(self):
        """Шаблон index сформирован с правильным контекстом."""
        response = self.guest_client.get(reverse('index'))
        first_object = response.context['page'][0]

        post_text_0 = first_object.text
        post_pub_date_0 = first_object.pub_date.date()
        post_author_0 = first_object.author.username
        post_group_0 = first_object.group.title
        self.assertEqual(post_text_0, self.post.text)
        self.assertEqual(post_pub_date_0, dt.date.today())
        self.assertEqual(post_group_0, self.post.group.title)
        self.assertEqual(post_author_0, self.post.author.username)
        self.assertContains(response, '<img')

    def test_group_correct_context(self):
        """Шаблон group сформирован с правильным контекстом."""
        response = self.guest_client.get(reverse(
            'group', kwargs={'slug': self.post.group.slug}))
        first_object = response.context['page'][0]
        group_title_0 = first_object.group.title
        group_slug_0 = first_object.group.slug
        group_description_0 = first_object.group.description
        self.assertEqual(group_title_0, self.post.group.title)
        self.assertEqual(group_slug_0, self.post.group.slug)
        self.assertEqual(group_description_0, self.post.group.description)
        self.assertContains(response, '<img')

    def test_post_only_in_one_group(self):
        """Созданный пост не появился на странице пустой группы"""
        response_emty_group = self.guest_client.get(reverse(
            'group', kwargs={'slug': self.empty_group.slug}))
        empty_group_obj = list(response_emty_group.context['page'].object_list)
        self.assertEqual(empty_group_obj, [])

    def test_new_post_correct_context(self):
        """Шаблон new_post сформирован с правильным контекстом."""
        response = self.authorized_client.get(reverse('new_post'))
        form_fields = {
            'group': forms.models.ModelChoiceField,
            'text': forms.fields.CharField
        }
        for value, expected in form_fields.items():
            with self.subTest(value=value):
                form_field = response.context['form'].fields[value]
                self.assertIsInstance(form_field, expected)
        self.assertIsInstance(response.context['form'], PostForm)

    def test_post_titles(self):
        """Посты с одним названием группы появились на главной
         и на странице групп"""
        response_post = self.guest_client.get(reverse('index'))
        post_object = response_post.context['page'][0]
        post_group_title_0 = post_object.group.title
        response_group = self.guest_client.get(reverse(
            'group', kwargs={'slug': self.post.group.slug}))
        group_object = response_group.context['page'][0]
        group_title_0 = group_object.group.title
        self.assertEqual(post_group_title_0, group_title_0)

    def test_post_edit_correct_context(self):
        """Шаблон post_edit сформирован с правильным контекстом."""
        response = self.authorized_client.get(reverse(
            'post_edit', kwargs={
                'username': self.post.author.username,
                'post_id': self.post.id}))
        form_fields = {
            'group': forms.models.ModelChoiceField,
            'text': forms.fields.CharField
        }
        for value, expected in form_fields.items():
            with self.subTest(value=value):
                form_field = response.context['form'].fields[value]
                self.assertIsInstance(form_field, expected)
        self.assertIsInstance(response.context['form'], PostForm)
        post_id_test = response.context['post_id']
        self.assertEqual(post_id_test, self.post.id)

    def test_profile_correct_context(self):
        """Шаблон profile сформирован с правильным контекстом."""
        response = self.guest_client.get(reverse(
            'profile', kwargs={'username': self.post.author.username}))
        first_object = response.context['page'][0]
        profile_text_0 = first_object.text
        profile_author_0 = first_object.author.username
        profile_group_0 = first_object.group.title
        profile_image_0 = first_object.image
        self.assertEqual(profile_text_0, self.post.text)
        self.assertEqual(profile_author_0, self.post.author.username)
        self.assertEqual(profile_group_0, self.post.group.title)
        self.assertEqual(profile_image_0, self.post.image)

    def test_single_post_correct_context(self):
        """Шаблон post сформирован с правильным контекстом."""
        response = self.guest_client.get(reverse(
            'post', kwargs={
                'username': self.post.author.username,
                'post_id': self.post.id}))
        first_object = response.context['post']
        post_text_0 = first_object.text
        post_author_0 = first_object.author.username
        post_group_0 = first_object.group.title
        self.assertEqual(post_text_0, self.post.text)
        self.assertEqual(post_author_0, self.post.author.username)
        self.assertEqual(post_group_0, self.post.group.title)
        self.assertContains(response, '<img')

    def test_cache_testing(self):
        """Проверка работы кэша"""
        template_key = make_template_fragment_key('index_page', [1])
        cache_data = cache.get(template_key)
        self.assertIsNotNone(cache_data)


class PaginatorViewsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        for i in range(13):
            Post.objects.create(
                text='Текст сообщения',
                pub_date=dt.date.today(),
                author=User.objects.create_user(
                    username='test_user' + str(i), ),
                group=Group.objects.create(
                    title='Тестовое название группы',
                    slug='test-slug' + str(i),
                    description='Тестовое описание группы'))

    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username='Artem')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_first_page_contains_ten_records(self):
        """На первой странице отображается 10 записей"""
        response = self.client.get(reverse('index'))
        self.assertEqual(len(response.context.get('page').object_list), 10)

    def test_second_page_contains_three_records(self):
        """На второй странице отображается 3 записи"""
        response = self.client.get(reverse('index') + '?page=2')
        self.assertEqual(len(response.context.get('page').object_list), 3)


class FollowPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user_1 = User.objects.create(username='user_1')
        cls.user_2 = User.objects.create(username='user_2')
        cls.user_3 = User.objects.create(username='user_3')

    def setUp(self):
        self.authorized_client_1 = Client()
        self.authorized_client_1.force_login(self.user_1)

        self.authorized_client_2 = Client()
        self.authorized_client_2.force_login(self.user_2)

        self.authorized_client_3 = Client()
        self.authorized_client_3.force_login(self.user_3)

        Post.objects.create(
            text='Текст сообщения',
            pub_date=dt.date.today(),
            author=self.user_1,
            group=Group.objects.create(
                title='Тестовое название группы',
                slug='test-slug',
                description='Тестовое описание группы',
            )
        )

    def test_follow(self):
        """Авторизованный пользователь может подписываться на авторов"""
        # Юзер 1 ни на кого не подписан
        follow_before = Follow.objects.filter(user=self.user_1).count()
        self.assertEqual(follow_before, 0)
        # Юзер 1 подписывается на юзера 2 через вьюху
        self.authorized_client_1.get(reverse(
            'profile_follow', kwargs={'username': self.user_2.username}))
        follow_after = Follow.objects.filter(user=self.user_1).count()
        self.assertEqual(follow_after, 1)

    def test_unfollow(self):
        """Авторизованный пользователь может отписываться от авторов"""
        # Создадими подписку программно, чтобы было от чего отписываться
        Follow.objects.create(user=self.user_1, author=self.user_3)
        # Посчитаем их
        follow_counts = Follow.objects.filter(user=self.user_1).count()
        # Отпишемся через вью
        self.authorized_client_1.get(reverse(
            'profile_unfollow', kwargs={'username': self.user_3.username}))
        # Посчитаем подписки и сравним их
        follow_after = Follow.objects.filter(user=self.user_1).count()
        self.assertEqual(follow_after, follow_counts - 1)

    def test_single_post_exist_in_followers(self):
        """Новый пост появялеется в ленте подписчика"""
        # Лента юзера 2 пустая
        response_emty_follow = self.authorized_client_2.get(
            reverse('follow_index'))
        empty_follow_obj = list(
            response_emty_follow.context['page'].object_list)
        self.assertEqual(empty_follow_obj, [])
        # Юзер 2 подписывается на юзера 1
        Follow.objects.create(user=self.user_2, author=self.user_1)
        response_follow_with_post = self.authorized_client_2.get(
            reverse('follow_index'))
        follow_obj_with_post = response_follow_with_post.context['page']
        # У юзера 2 в ленте появляется пост юзера 1
        self.assertEqual(len(follow_obj_with_post.object_list), 1)

    def post_not_in_uhfollower_page(self):
        """Созданный пост не появляется в ленте неподписанного
        пользователя"""
        # Лента юзера 3 пустая после создания поста юзера 1
        response_emty_follow_3 = self.authorized_client_3.get(
            reverse('follow_index'))
        empty_follow_obj_3 = list(
            response_emty_follow_3.context['page'].object_list)
        self.assertEqual(empty_follow_obj_3, [])


# скопировал из test_models.py
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
        form_data = {
            'post': self.post,
            'author': self.user_2,
            'text': 'Тестовый комментарий'
        }
        response = self.authorized_client_2.post(
            reverse('add_comment', kwargs={
                'username': self.post.author.username,
                'post_id': self.post.id}),
            data=form_data,
            follow=True
        )
        comments_after = Comment.objects.filter(author=self.user_2).count()
        # Количество комментариев юзера 2 стало больше ровно на одну штуку
        self.assertEqual(comments_after, comments_before + 1)
        # Существует созданный пост с теми данными,
        # которые мы передавали в POST
        self.assertTrue(Comment.objects.filter(
                        post=form_data['post'],
                        author=form_data['author'],
                        text=form_data['text']
                        ).exists())
        self.assertIsInstance(response.context['form'], CommentForm)
        self.assertIsInstance(response.context['post'], Post)
