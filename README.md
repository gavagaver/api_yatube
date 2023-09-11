# REST API для Yatube
[![CI](https://github.com/gavagaver/api_yatube/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/gavagaver/api_yatube/actions/workflows/tests.yml)

«API для Yatube» позволяет пользователям социальной сети [Yatube](https://github.com/gavagaver/yatube)  публиковать свои посты и управлять подписками через программный интерфейс взаимодействия.

## Возможности:

- Получение, создание, обновление, удаление публикаций.
- Получение, создание, обновление, удаление комментариев к публикациям.
- Просмотр сообществ и детальной информации о них.
- Отслеживание подписок на авторов, а так же возможность подписки на интересующего автора.
- Получение, обновление и проверка JWT авторизации.

## Установка и запуск:
1. [ ] Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/gavagaver/api_yatube.git && cd api_yatube
```

1. [ ] Создать и активировать виртуальное окружение:

###### Windows:
```bash
python -m venv venv
```
```bash
source venv/Scripts/activate
```
```bash
python -m pip install --upgrade pip
```
###### Linux:
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
python3 -m pip install --upgrade pip
```

1. [ ] Установить зависимости
```bash
pip install -r requirements.txt
``` 
1. [ ] Перейти в папку с manage.py

```bash
cd api_yatube
``` 

1. [ ] Создать миграции
###### Windows:
```bash
python manage.py makemigrations
```
###### Linux:
```bash
python3 manage.py makemigrations
```

1. [ ] Применить миграции
###### Windows:
```bash
python manage.py migrate
```
###### Linux:
```bash
python3 manage.py migrate
```

1. [ ] Создать супер-пользователя
###### Windows:
```bash
python manage.py createsuperuser
```
###### Linux:
```bash
python3 manage.py createsuperuser
```

1. [ ] Запустить проект
###### Windows:
```bash
python manage.py runserver
```
###### Linux:
```bash
python3 manage.py runserver
```

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

## Стек
- Python 3.7
- Django 2.2
- Django REST Framework
- SQLite3
- Simple-JWT

## Об авторе
Голишевский Андрей Вячеславович  
Python-разработчик (Backend)  
E-mail: gav@gaver.ru  
Telegram: @gavagaver  
Россия, г. Москва  
