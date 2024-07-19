# API для Yatube
**RU**
## Описание

Yatube - это блог для публикации постов и комментариев, нацеленный по концепции на обсуждение фильмов. Проект состоит из бекенда на Django и фронтенда на React.

**API для проекта Yatube - это решение готовое к взаимодействию с фронтендом блога Yatube, где у пользователей есть следующие возможности:**
* регистрация
* публикация постов
* публикация комментариев
* подписка на публикации прочих пользователей сервиса

В данном проекте моей главной задачей было написать API бекенда сервиса для осуществления взаимодействия с фронтендом на React.
Бекенд был мною разработан на Django REST Framework.
Тистирование API в ходе разработки я проводил в Postman.
Также в проекте я настраивал CI/CD - составлял Dockerfile, конфигурацию файлов Nginx локального и на сервере с Ubuntu (поскольку на сервере развернуто несколько проектов в контейнерах), также настраивал автоматический деплой на сервер с помощью GitHub workflows.


## Стек технологий проекта
![Python](https://img.shields.io/badge/-Python-black?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/-Django-black?style=for-the-badge&logo=Django)
![DRF](https://img.shields.io/badge/-Django_REST_Framework-black?style=for-the-badge&logo=DRF)
![PostgresQL](https://img.shields.io/badge/-PostgresQL-black?style=for-the-badge&logo=PostgresQL)
![SQLite](https://img.shields.io/badge/-SQLite-black?style=for-the-badge&logo=SQLite)
![Docker](https://img.shields.io/badge/-Docker-black?style=for-the-badge&logo=Docker)
![Nginx](https://img.shields.io/badge/-Nginx-black?style=for-the-badge&logo=Nginx)
![Linux](https://img.shields.io/badge/-Linux-black?style=for-the-badge&logo=Linux)
![Postman](https://img.shields.io/badge/-Postman-black?style=for-the-badge&logo=postman)

## Установка

***Клонировать репозиторий и перейти в него в командной строке:***

git clone 
cd kittygram
Cоздать и активировать виртуальное окружение:
```
git clone git@github.com:your_username_in_github/api_final_yatube.git
python -m venv env
source venv/Script/activate
```
***Установить зависимости из файла requirements.txt:***

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

***Выполнить миграции:***

```
python manage.py migrate
```

***Запустить проект:***

```
python manage.py runserver
```
