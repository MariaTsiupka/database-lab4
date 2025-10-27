# Беремо базовий образ Python
FROM python:3.11-slim

# Робоча папка – батьківська для пакета auth
WORKDIR /app/my_project

# Встановлюємо системні залежності для mysqlclient та flask-mysqldb
RUN apt-get update && \
    apt-get install -y build-essential default-libmysqlclient-dev pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Копіюємо requirements.txt і встановлюємо залежності
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь проект
COPY my_project ./my_project

# Відкриваємо порт для Flask
EXPOSE 5000

# Запуск додатка як модуля – так працюють відносні імпорти
CMD ["python", "-m", "my_project.auth.app"]

