FROM python:3.9

COPY . /app

RUN make /app

CMD python3 /app/http_proxy.py