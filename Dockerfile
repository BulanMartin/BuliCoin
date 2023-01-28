FROM python:3.10

WORKDIR /bulicoin_server

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /bulicoin_server

RUN pip install --upgrade pip

RUN pip install -v -r requirements.txt

COPY ./bulicoin_server /bulicoin_server

#WORKDIR /bulicoin_server/flaskr

EXPOSE 5000

CMD ["flask", "--app", "flaskr", "--debug", "run", "--host=0.0.0.0", "--port=5000"]
#CMD ["python", "server.py"]