FROM  python:alpine3.12

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "./run.py"]