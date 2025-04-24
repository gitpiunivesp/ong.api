FROM python:alpine

RUN apk add build-base libpq libpq-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["flask", "--app", "src.main", "run", "-h", "0.0.0.0"]
