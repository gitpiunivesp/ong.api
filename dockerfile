FROM python:3.11-alpine

WORKDIR /app

RUN apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    postgresql-dev \
    build-base

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["flask", "--app", "src.main", "run", "-h", "0.0.0.0"]
