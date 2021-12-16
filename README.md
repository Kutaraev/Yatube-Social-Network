[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)

# Yatube Social Network
Социальная сеть Yatube

## Содержание
- [Описание](#Описание)
- [Технологии](#Технологии)
- [Установка](#Установка)
- [Примеры](#Примеры_страниц_приложения)
- [Планы](#Планы_по_развитию_проекта)
- [Контакты](#Контакты)

### <a name="Описание">Описание</a>
Базовый проект социальной сети для публикации дневников и заметок. Содержит в себе все, что нужно для создания минималистичного онлайн-сервиса, в котором пользователи могут излагать свои мысли, идеи и мнения. Структура программы обладает гибкостью и легко может быть изменена, а также дополнена новыми возможностями. Функции проекта, доступные при запуске:
- Регистрация пользователей;
- Публикация текстовых заметок с возможностью добавить изображение;
- Комментирование чужих записей;
- Добавление публикаций в тематическую группу, заранее созданную администратором;
- Возможность подписаться на любимых авторов.

### <a name="Технологии">Технологии</a>
- [Python 3](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Git](https://github.com/)
- [Visual Studio Code](https://code.visualstudio.com/Download)

## Установка
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

## Примеры страниц приложения
В данном разделе находятся основные структурные элементы, из которых состоит данный проект.
### Страница регистрации
![регистрация](https://lh3.googleusercontent.com/wEAU6LgmMUJFfUEUcCQ3O7fsqslV2acBOGs0HS7f6LkHzAwAcZTk0_pC3PvBhhFunJVBp4TYHbeN2sFWaQ8WPPsYuDGCVz7NTdEpPIruoC5cB1LlllPksQQU-GuqtrXOGxRaviBDNaCAX8lio5bq6p6nZdt23vNxT5svH1z7a3u9rC9xoziN1IF1n1IBh9Oaxv4MHPQga3xj8L3jDtSRFhmpnn6DafgIzvGHVhqLQ1_BVtYziPiFBpk_6_RobxkoVqp9mMIPrK6qGhjCXY9ZwFM7-9nDkDjE0u89CKCp6AMFcDnZh9DsCORXtFbMMINS6A30z2cI76tHHQn8-QMi1CKSPpVwTrbGn_3fS5dQmREQFnZq2PHn2QBPsfXV4VGyzYAzSenqRnVU9er_W3cOKmLyeaMD8qBOj8-uO1zwUXuEDWxdQpiZE-Q3CuTOQvNkB4KMitTHG8SS1GFv7zLl7pDt_LJa8ARYdlkoDbrgIDorRJ2na5mzp10TDY3Ao0bSz7oCE8DfEGeEoXBJza3JaTmB716hv_6N0-OPVri7l_FMH9E8Ov06hOYyUw_QfrYETob1hMA8hisWrZEJhCONqgOhXtdFP8W72WmDr6I_5E2aE2RP6t7Da1PBpbznTNM6W4wLdpEOhej6X9C_hN7DGTE3u9F_lEDVv8EI_Trfuqan1xC56TJVfji2UGw-c_-dKPJWUIbct0qiCFM4kd0gtIan=w694-h791-no?authuser=0)
### Главная страница
![главная](https://lh3.googleusercontent.com/m_z_w7cRLDKOGw1mRiYmxyqI1V4ogY0qJ94dNbB05JnJbb68Vrk0IfcWdNoXYSL72INfLO4u8vhtO2NKOiA7ap5JtveaE1-_cdFaArkizTQvwMxWhC1A5gSzxD2ias5mI97WQ5WAeTIAyXpfPHRBbPVw3Os4ehscplFDVJpGwrnBMI__TGlIjXNC1db_0seLSm4C_htB5VRRilrXRG3QzU0LV2I9s5JKD9F_-IpY4K5KZ2d0avQ0jgpU6-1txJqrjUXTftRBWdOaiuKZt1Lx6QIzm_p3_ZARmGKMzWRNZNwhL4pgbiG_IJneQhFCgGNh_0pzosM0Fs9RfLamn3rCpX5n4aaWT_1r7v8rtD6TnJuxBlCr813NTLo-1ozvW7Z1FU6e2VJsPsarQ30834Y8M9C9p0aTYkR4asX4VCbW-bRuqtZhjtD7YXC8VJ757GqWN1aIbzYij8VgcejV_OPZl0GYC5oXSHZ5bP9Q7QWB3CEd-ro2eo8OozwuU3Tzr245xroHUdIUdw_J0doa02L7c0avgXWP2RO3A_FHfoL6zSij9x3sy0cV-9hp-klwlU5bKcagRUzFHNvZJ94MT7rxlECZXyFiWjfOgSk5z7YuYCsobAtC5Qz5yFBjgKt0V13XLIkIxrQH4qG4F3ouCaiLT4dxOfB36aeNjzb9IdPYRCnnXyL0bOnYIAOXy3FA03Suk-qFXVxgERGSG4txtL1aLo7l=w902-h853-no?authuser=0)
### Тематические группы
![группы](https://lh3.googleusercontent.com/v0pdWlt7tnMTYyClbHyFIRjfumJS0u-8S8JiEZ5V55QFe_F5oGktnhiAMFJis6Sj1KNL6cV3eJZS8STud2bkzrxVGgCHMkrSl9OKaSaMS2jBrKnDRhr0p8J_LFHTt01q9DSUpIgG6F395MCTo1npBClzD8zPn0bJXJLyvszWT44xSK7JDhJztdJUxnDKHpCI82exIyainE5RYgBjiB4DgnyBvZPxAmpcpADPDWjWaxy20dmrilGkfiNliY170qfkRMrUn5XVAIExp2KK_1Z2w_Ov1y0AJUc5VO4JutU5AloTqQIWYbqvXNjOszUnf1_-AGjrBZ-b6ampk-fmGxTDwJ5zwnm9zZuxxDSHp2wNF_XwzbHmOrj9LSPgalcDBIgvgR2WWrBqq_LaiJHRw5U32W_0oehe8q5wHhqIq6gM1c2t_o9L3Vu3ojcetTcnzw7UxK2RqqMcX2A_jYVArXAPtiX1Sqlc_1XfvVO0Rg1C637njEgWVxWPi_6bGlgL4pzIVcmK-PTDdaP-GXxLslQVyKa___gYfBRuLiDq5qbT-VtUBGvhZKTA0bcs435BCijtWHTPzWeq4LUuQMFRJn84RrDGzBDLwkxar0plxN5CAfV97OoXif-viJBJoyS2QO6n0Er8ni_sMK1kL1LspX_4N5vYoPvOsvsOi6xwiePIEQCfTMMw8F94_uQXa2x4t76FBeFltp_50RaefXHjeh-0oQoa=w891-h698-no?authuser=0)
### Страница пользователя
![пользователь](https://lh3.googleusercontent.com/hBCSxYu1iSRNClYKQt8v9rjn-KtXUPn_3zBVEGTKJvDf8mrSfxCxaVTzBTerhdTur6DIdXmnyqKAajtjR8waCURhD-InrvTa8vyNI8mselEDEMGTDY65wacBvBySSByEO7j_FICjpsACNc8VD-89O3y3dcg-nnYxt5lQo84NkffVa-1D_o3tD4Ni0AjyFA6BfLIlivq6SPHCm8n4OBQ4rTnlgo2Cqrv0KWo7jkE5sDd5a7WUfK_BClkilbTGlcvP6Y0j8vCBAQ-9pDXF3kYVy0at-0mFDwuB_RX8qCfW9F6z_uWPC9JnKOew5PHtCf7_cBNaXx-bFD5vKnGKTw0oTAI2hvB6bo-Qe8V2GjgcuhcC52_m7IH7l-pFSq9fsEb80gZD3zqVl9ymozAAvn3J3NBcvE1B8gu7LlCRa5fGZJvYrgkaaxVfSPK0GVaEWu5YyzFm8hTHYhiitDgh8iVQpr8iSK0oNTA4GKA8ZlMxwR1LvSqnibsQ38LDipy5HV4iKdcuFrNSC_kLgiox64uHAggJMEwWqj0iwugMNyhPvLZjytEcPBcniFJc-RyeyPBMs4dvLTb83Zt6_x_i-xHn5AJ7GAzCxWRqWrjcIYZzqfp1cKIuvWVdAtT-Giu_cGVh2tEv-mPba3Erzd0aMGQaokeB0G3EEg99olvgvhvjsE8E1vLyTbz9aCkPzHzU5FAPZ_Az1U6uSGobxdEDaL9M7xoP=w1150-h732-no?authuser=0)
### Блок комментариев
![комментарии](https://lh3.googleusercontent.com/XlfA61zRG5wwkIMPe3abnBHzmYYJcjDLaSSUrfq9iIyFSxzPk8z-wzQeL-HC_n9Tm7tSiZkS9b88Ul_-yQj1DmVSLKvVdZQCgiEzLoPOvkutx1aluJI9EWy5o0N9F2uVcp50t5iLrckMSwDVKniF3VB2o7vf-oDaUA2p1firCuAd9wRJFvd42vekjCUUXdvVNJOZBdnulsyAcZPHxVo4D5HZt5x4sG1nDwg6JmU0FvmeoLIAWKFli_VoRJqazlKE119SZj3uS-5bpbtCGMGVBYgr9geUPMqMcwTw9pjB2PYwgskS24buOxrxFYh8JgXcNG2hqryD2mOOMv7dCPGCk-zliFwInoK6DLUJ0rZJx3QZnkWDE5qWSjICBQ4bzKdONj1yR4UVTj_ZyKKMGLnvDuJz51D7Fl-hqrGCQNbzOb81KrIFIjiAfCbt5pBUUwwqP34dI5e6wTdHmpjql5CGqbYnyyzY6nq0SrqGMHK4M-sJySPvSG0ejEJidSj3ugWIs5b7NJBXnewamYU1PtFX7RK9n-w4NiuFaFoyP1V44JVrE34dS3W250iAmY_5VYAdDOZQe6DeBElFiTfA8cOunq6c0OGlURm7PQjXHHBAxrjR4IhBa-oe4g2ptiHPx7qaj0Cp-f8k_kwbw8OBRQ-OE_sw8g5uRmMQ4ifkj74R-boAr0AEd0w05gbIkqSrzPZrb8x-_vw63rnWh0y2BiunG2Wd=w518-h857-no?authuser=0)
## Планы по развитию проекта
Несмотря на то, что проект полностью готов к деплою на сервер и собственно запуску, он содержит лишь базовые элементы социальной сети: посты и комментарии.Функционал можно расширить следующим образом:
- Создание более детальной и информативной страницы пользователя, в которой он может оставить свои контактные данные и информацию о себе;
- Создание системы рейтингов постов и комментариев;
- Добавление на главную страницу строки поиска и разработка системы тегов, при помощи которой можно найти тематические посты.
- Создание новостной ленты, контент которой создают модераторы.

## Контакты
Артем Кутараев – [@artem_kutaraev](https://t.me/artem_kutaraev) – artem.kutaraev@gmail.com  
Ссылка на проект – [https://github.com/Kutaraev/Yatube-Social-Network.git](https://github.com/Kutaraev/Yatube-Social-Network.git)
