
FROM python:3.11-slim

WORKDIR /app/my_project

# Встановлюємо системні залежності для mysqlclient та flask-mysqldb
RUN apt-get update && \
    apt-get install -y build-essential default-libmysqlclient-dev pkg-config && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY my_project ./my_project


EXPOSE 5000

CMD ["python", "-m", "my_project.auth.app"]

