# Проект «API для Yatube»
[![CI](https://github.com/gavagaver/api_yatube/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/gavagaver/api_yatube/actions/workflows/tests.yml)
«API для Yatube» позволяет пользователям социальной сети Yatube публиковать свои посты и управлять подписками через программный интерфейс взаимодействия.

## Функции:

- Получение, создание, обновление, удаление публикаций.
- Получение, создание, обновление, удаление комментариев к публикациям.
- Просмотр сообществ и детальной информации о них.
- Отслеживание подписок на авторов, а так же возможность подписки на интересующего автора.
- Получение, обновление и проверка JWT авторизации.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/gavagaver/api_final_yatube.git`

`cd api_final_yatube`


Создать и активировать виртуальное окружение:

+ `python -m venv venv`
+ `source venv/Scripts/activate`
+ `python -m pip install --upgrade pip`

Установить зависимости из файла requirements.txt:
`pip install -r requirements.txt`

Выполнить миграции:
`python manage.py migrate`


Запустить проект:
`python manage.py runserver`

После запуска проекта, документация будет доступна по адресу:
`http://localhost:port/redoc/`

## Примеры запросов:

### GET-запрос, получение информации о сообществе c id=1

`GET http://localhost:port/api/v1/groups/1/`

#### Ответ:

```
{
    "id": 2,
    "title": "second group",
    "slug": "second-group",
    "description": "second group description",
}
```

### POST-запрос на добавление новой публикации (требуется токен)

`POST http://localhost:port/api/v1/posts/`

```
{
  "text": "Текст поста",
  "group": 1
}
```

#### Ответ:

```
{
    "id": 1,
    "author": "root",
    "text": "Текст поста",
    "pub_date": "2023-01-01T08:31:16.164522Z",
    "image": null,
    "group": 1
}
```



