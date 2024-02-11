FROM  python:3.11-alpine

ENV TEST_BASE_PATH=/app/resources/base_teste.txt

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

