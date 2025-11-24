# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /proj/api_llm

# Копируем файлы приложения
COPY . .

# Устанавливаем зависимости
RUN apt update -y
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду для запуска приложения
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "api_llm:llm", "--bind", "0.0.0.0:8000"]
