FROM python:3.14-alpine3.22

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask redis

EXPOSE 5000

CMD ["flask", "--app", "hello", "run", "--host=0.0.0.0"]
