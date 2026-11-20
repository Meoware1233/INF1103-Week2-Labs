FROM python:3.11-slim

WORKDIR /app

COPY . .

CMD ["python", "week11_main.py"]