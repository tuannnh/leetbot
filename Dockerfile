FROM python:3.9-slim

WORKDIR /app

copy requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ../leetbot-old .

EXPOSE 8000

CMD ["python", "app/main.py"]
