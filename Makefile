.PHONY: check makemigrations migrate full-migrate verify

# Проверка системных проверок Django (без миграций)
check:
	docker compose exec django python manage.py check

# Создание миграций только для приложения core
makemigrations:
	docker compose exec django python manage.py makemigrations core

# Применение всех миграций к БД
migrate:
	docker compose exec django python manage.py migrate

# Полный цикл для локальной разработки: проверка → миграция → применить
full-migrate: check makemigrations migrate

# Для CI и проверки перед коммитом: убедиться, что нет изменений без миграций
verify:
	docker compose exec django python manage.py makemigrations --check
