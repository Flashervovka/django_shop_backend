.PHONY: check makemigrations migrate full-migrate verify up down logs

# Проверка системных проверок Django (без миграций)
check:
	docker compose run --rm django python manage.py check

# Создание миграций только для приложения core
makemigrations:
	docker compose run --rm django python manage.py makemigrations core

# Применение всех миграций к БД
migrate:
	docker compose run --rm django python manage.py migrate

# Полный цикл: проверка → создание миграций → применение
full-migrate: check makemigrations migrate

# Для CI и перед коммитом: убедиться, что нет изменений без миграций
verify:
	docker compose run --rm django python manage.py makemigrations --check --dry-run

# Быстрый запуск всех сервисов
up:
	docker compose up -d

# Остановка всех сервисов
down:
	docker compose down

# Просмотр логов Django в реальном времени
logs:
	docker compose logs -f django
# Полный сброс и пересоздание окружения (использовать редко!)
reset-full:
	@echo "Full environment reset: stopping, migrating, starting..."
	make down
	make full-migrate
	make up