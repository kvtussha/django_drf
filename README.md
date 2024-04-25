# Запуск проекта Django с использованием Docker Compose

Этот проект представляет собой шаблон для запуска Django приложения в среде Docker с использованием Docker Compose.

# Предварительные требования

Убедитесь, что у вас установлены следующие компоненты:

- Docker: [установка Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [установка Docker Compose](https://docs.docker.com/compose/install/)

# Запуск проекта

## Клонируйте репозиторий
git clone https://github.com/kvtussha/django_drf

## Перейдите в директорию проекта
cd yourproject

## Скопируйте файл .env.example в .env и настройте его
cp .env.example .env

## Запустите контейнеры с помощью Docker Compose
docker-compose up --build -d

## Примените миграции Django
docker-compose exec web python3 manage.py migrate

### Управление контейнерами

```bash
# Остановить контейнеры
docker-compose down

# Просмотреть журналы контейнера Django
docker-compose logs -f web
