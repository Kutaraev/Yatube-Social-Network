[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)

# Yatube Social Network
Социальная сеть Yatube

## Содержание
- [Описание проекта](#Описание)
- [Технологии](#Технологии)
- [Установка](#Установка)
- [Примеры страниц приложения](#Примеры)
- [Планы по развитию проекта](#Планы)
- [Контакты](#Контакты)

## <a name="Описание">Описание</a>
Базовый проект социальной сети для публикации дневников и заметок. Содержит в себе все, что нужно для создания минималистичного онлайн-сервиса, в котором пользователи могут излагать свои мысли, идеи и мнения. Структура программы обладает гибкостью и легко может быть изменена, а также дополнена новыми возможностями. Функции проекта, доступные при запуске:
- Регистрация пользователей;
- Публикация текстовых заметок с возможностью добавить изображение;
- Комментирование чужих записей;
- Добавление публикаций в тематическую группу, заранее созданную администратором;
- Возможность подписаться на любимых авторов.

## <a name="Технологии">Технологии</a>
- [Python 3](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Git](https://github.com/)
- [Visual Studio Code](https://code.visualstudio.com/Download)

## <a name="Установка">Установка</a>
1. Клонировать репозиторий
```
git clone https://github.com/Kutaraev/Yatube-Social-Network.git
```
2. Создать виртуальное окружение
```
python -m venv venv
```
3. Активировать виртуальное окружение
```
source venv/scripts/activate
```
4. Установить необходимые пакеты для работы приложения из файла зависимостей
```
pip install -r requirements.txt
```

## <a name="Примеры">Примеры страниц приложения</a>
В данном разделе находятся основные структурные элементы, из которых состоит данный проект.
### Страница регистрации
![регистрация](https://lh3.googleusercontent.com/YMm1ztJoWZZWG8QxokvtJWeFy7jEkvPX2QD5yoz-XEFeEspexd6PYBXfAWo2pNmLZ2ThpuG3ZBkjRFbYyXc=w193-h220-rw)
### Главная страница
![главная](https://lh3.googleusercontent.com/VgNwk2SAj4MpjxGUTdba22BBt6qtHdcsc0qF1m10Jk2IulwS5ORzOpcxHn4w64UdC95kHF_X6Uwva633tWU=w233-h220-rw)
### Тематические группы
![группы](https://lh3.googleusercontent.com/OttRtjxdJBpb9xoqNSOdU8dZKbpm4OgNdB8wABvL7YJ1CtsynMztO8zRTUbyucudgTfmgigwuvrj6i913qc=w281-h220-rw)
### Страница пользователя
![пользователь](https://lh3.googleusercontent.com/QEuD5tzVZuNaXtkkUgHgUyGS6fXjncQX6bcZnf8gLGVsN1ZAKmUYS1EOpqOtsTex-iJ-VH5J5vDTtY_nio8=w346-h220-rw)
### Блок комментариев
![комментарии](https://lh3.googleusercontent.com/y_-ZkLgHOj6ebJR8G9-lSZy-XbWI5TPi9Go0tPPQhHqDouSpzLBb4vNN3LuX2f5wttT7-Nrj5xgdiK7BnDw=w133-h220-rw)
## <a name="Планы">Планы по развитию проекта</a>
Несмотря на то, что проект полностью готов к деплою на сервер и собственно запуску, он содержит лишь базовые элементы социальной сети: посты и комментарии.Функционал можно расширить следующим образом:
- Создание более детальной и информативной страницы пользователя, в которой он может оставить свои контактные данные и информацию о себе;
- Создание системы рейтингов постов и комментариев;
- Добавление на главную страницу строки поиска и разработка системы тегов, при помощи которой можно найти тематические посты.
- Создание новостной ленты, контент которой создают модераторы.

## <a name="Контакты">Контакты</a>
Артем Кутараев – [@artem_kutaraev](https://t.me/artem_kutaraev) – artem.kutaraev@gmail.com  
Ссылка на проект – [https://github.com/Kutaraev/Yatube-Social-Network.git](https://github.com/Kutaraev/Yatube-Social-Network.git)
