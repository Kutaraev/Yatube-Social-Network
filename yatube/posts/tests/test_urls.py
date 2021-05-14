import datetime as dt
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from ..models import Group, Post

User = get_user_model()


class StaticURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.post = Post.objects.create(
            text='Текст сообщения',
            pub_date=dt.date.today(),
            author=User.objects.create_user(username='test_user', ),
            group=Group.objects.create(
                title='Тестовое название группы',
                slug='test-slug',
                description='Тестовое описание группы'
            )
        )

        cls.group = Group.objects.create(
            title='Название группы',
            description='Описание группы',
            slug='test_slug'
        )

        cls.user_another = User.objects.create_user(
            username='AnotherTestUser')

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.post.author)

        self.authorized_client2 = Client()
        self.authorized_client2.force_login(self.user_another)

    def test_home_url_exists(self):
        """ Главная страница доступна любому пользователю"""
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_group_url_exists(self):
        """ Страница групп доступна любому пользователю"""
        response = self.guest_client.get(f'/group/{self.group.slug}/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_new_post_authorized(self):
        """ Страница создания поста доступна только
        авторизованному пользователю"""
        response = self.authorized_client.get('/new/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_new_post_redirect_anonymous(self):
        """Страница создания поста перенаправит неавторизованного
        пользователя на страницу логина"""
        response = self.guest_client.get('/new/', follow=True)
        login = reverse('login')
        my_target_url = '/new/'
        self.assertRedirects(
            response, f'{login}?next={my_target_url}')

    def test_urls_templates_correct(self):
        """URL-адрес использует соответствующий шаблон"""
        templates_url_names_guest = {
            'index.html': '/',
            'group.html': f'/group/{self.group.slug}/',
        }
        for template, adress in templates_url_names_guest.items():
            with self.subTest(adress=adress):
                response = self.guest_client.get(adress)
                self.assertTemplateUsed(response, template)

        response_new = self.authorized_client.get('/new/')
        self.assertTemplateUsed(response_new, 'new_post.html')

        response_edit = self.authorized_client.get(
            f'/{self.post.author.username}/{self.post.id}/edit/')
        self.assertTemplateUsed(response_edit, 'new_post.html')

    def test_profile_page_exists(self):
        """Проверка доступности страницы пользователя"""
        response = self.guest_client.get(
            f'/{self.post.author}/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_single_post_exists(self):
        """Проверка доступности отдельного поста"""
        response = self.guest_client.get(
            f'/{self.post.author.username}/{self.post.id}/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_edit_for_anonimous(self):
        """Проверка доступности редактирования поста для
        анонимного пользователя"""
        login = reverse('login')
        my_target_url = f'/{self.post.author.username}/{self.post.id}/edit/'
        response = self.guest_client.get(my_target_url)
        self.assertRedirects(
            response, f'{login}?next={my_target_url}')

    def test_post_edit_for_author(self):
        """Проверка доступности редактирования поста для автора"""
        response = self.authorized_client.get(
            f'/{self.post.author.username}/{self.post.id}/edit/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_edit_for_another_user(self):
        """Проверка доступности редактирования поста
        для другого пользователя"""
        response = self.authorized_client2.get(
            f'/{self.post.author.username}/{self.post.id}/edit/')
        self.assertRedirects(
            response, f'/{self.post.author.username}/{self.post.id}/')

    def test_404_url_exists(self):
        """ Сервер возвращает 404 при неизвестной сранице"""
        response = self.guest_client.get('/very_bad_page/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_comment_redirect(self):
        """Страница создания комментария перенаправит неавторизованного
        пользователя на страницу логина"""
        login = reverse('login')
        my_target_url = f'/{self.post.author.username}/{self.post.id}/comment'
        response = self.guest_client.get(my_target_url)
        self.assertRedirects(
            response, f'{login}?next={my_target_url}')

    # Добавил проверку на редирект
    def test_follow_redirect(self):
        """Страница ленты подписок перенаправит неавторизованного
        пользователя на страницу логина"""
        login = reverse('login')
        my_target_url = '/follow/'
        response = self.guest_client.get(my_target_url)
        self.assertRedirects(
            response, f'{login}?next={my_target_url}')
