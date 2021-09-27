# hw05_final
Социальная сеть Yatube

## Описание
Проект представляет собой социальную сеть. В Yatube пользователи могут создать собственную страничку, публиковать записи в тематические группы, подписываться на любимых авторов.

## Перечень технологий, используемых в проекте
1. Python 3.8.4
2. Django 2.2.6
3. Pillow==7.0.0
4. Sorl-thumbnail==12.6.3
5. Visual Studio Code

## Установка

1. Клонировать репозиторий:
```
    git clone https://github.com/Kutaraev/hw05_final.git
```
2. Создать виртуальное окружение:
```
    python -m venv venv
```
3. Активировать виртуальное окружение:
```
    source venv/scripts/activate
```
4. Установить зависимости из requirements.txt
```
pip install -r requirements.txt
```
5. Запустить сервер
```
python manage.py runserver
```

## Функционал
### Регистрация пользователя
Здесь пользователь вводит данные, необходимые для регистрации.


![страница регистрации](http://surl.li/ahmbb)


### Главная страцица
На главной странице показаны последние публикации пользователей. Под каждым постом есть кнопка "Коммертировать", и "Редактировать" - если залогиненый пользователь является автором поста.


![главная страница](http://surl.li/ahmbl)


### Тематические группы
На старнице опубликованы посты определенной категории. Категории постов создает администратор.


![группы](http://surl.li/ahmbo)


### Страница пользователя
Профиль пользователя с возможностью просмотра опубликованных постов и их общего количества, а так же подписчиков и подписок.


![профиль](http://surl.li/ahmss)


### Комментарии
Здесь отображены все комментарии к посту, а также форма для записи нового комментария.


![комментарии](http://surl.li/ahmsv)



