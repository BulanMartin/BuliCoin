FROM python:3.10

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /src

RUN pip install -v -r requirements.txt

COPY ./src /src

EXPOSE 5000

CMD ["python", "server.py"]