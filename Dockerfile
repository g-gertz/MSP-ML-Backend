FROM python:3.12-slim
LABEL authors="g-gertz"

EXPOSE 9999

WORKDIR /app

COPY requirements.txt /app

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

RUN pip install --no-cache-dir -r requirements.txt

COPY api /app/api
COPY core /app/core

COPY .env /app
COPY loss_functions.py /app
COPY main.py /app

CMD ["python", "main.py"]
