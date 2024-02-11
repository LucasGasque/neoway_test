FROM  python:3.11-alpine

ENV TEST_BASE_PATH=/app/resources/

WORKDIR /app

COPY . /app

RUN apk add --no-cache postgresql-dev
RUN apk add build-base
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./run.py"]