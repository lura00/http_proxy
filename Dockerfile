FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

ENV PORT=8000

EXPOSE 8000

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "./app/http_proxy.py"]


# If you beeing refused connection by Docker daemon, try type in cli, sudo chmod 666 /var/run/docker.sock
