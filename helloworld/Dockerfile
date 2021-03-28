FROM python:3-slim-buster

ARG VERSION=latest

RUN pip install flask
RUN pip install flask_restful

ENV VERSION=$VERSION

ADD helloworld.py /

EXPOSE 8080

CMD [ "python", "./helloworld.py"]
