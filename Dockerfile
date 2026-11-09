FROM python:3.12-slim

WORKDIR /app

# Установка системных зависимостей: и для psycopg2, и для Pillow
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Команда будет переопределена в docker-compose для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
