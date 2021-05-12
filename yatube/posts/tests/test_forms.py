import datetime as dt
import shutil
import tempfile
from http import HTTPStatus

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Post, Group

User = get_user_model()


class NewPostFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        settings.MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username='Artem')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_create_new_post(self):
        """Проверка создания записи в БД при отправке формы"""
        group = Group.objects.create(
            title='Название группы',
            description='Описание группы',
            slug='test_slug'
        )
        posts_count = Post.objects.count()

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

        form_data = {
            'group': group.id,
            'text': 'Текст нового сообщения',
            'image': uploaded
        }

        response = self.authorized_client.post(
            reverse('new_post'),
            data=form_data,
            follow=True
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertRedirects(response, reverse('index'))
        self.assertEqual(Post.objects.count(), posts_count + 1)
        self.assertTrue(Post.objects.filter(
                        group=form_data['group'],
                        text=form_data['text'],
                        image='posts/small.gif'
                        ).exists())

    def test_post_edit(self):
        """Проверка редактирования поста"""
        post = Post.objects.create(
            text='Текст сообщения',
            pub_date=dt.date.today(),
            author=self.user,
            group=Group.objects.create(
                title='Тестовое название группы',
                slug='test-slug',
                description='Тестовое описание группы'
            ))
        posts_count = Post.objects.count()

        form_data = {
            'group': 1,
            'text': 'Текст сообщения_измененный'
        }

        response = self.authorized_client.post(
            reverse('post_edit', kwargs={
                'username': post.author, 'post_id': post.id}),
            data=form_data,
            follow=True
        )
        first_object = Post.objects.first()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertRedirects(response, reverse(
            'post', kwargs={'username': post.author, 'post_id': post.id}))
        self.assertEqual(Post.objects.count(), posts_count)
        self.assertEqual(first_object.group.id, post.id)
        self.assertEqual(first_object.text, form_data['text'])
