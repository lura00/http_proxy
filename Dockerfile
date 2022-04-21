FROM python:3.9

WORKDIR /usr/src/app

COPY . /app

RUN make /app

CMD python3 /app/http_proxy.py