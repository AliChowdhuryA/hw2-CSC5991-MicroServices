# syntax=docker/dockerfile:1
FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]


COPY requirements.txt requirements.txt