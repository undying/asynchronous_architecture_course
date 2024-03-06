FROM python:3.12.2

COPY src/requirements.txt /opt/app/
WORKDIR /opt/app

RUN pip install -r requirements.txt
COPY src/ /opt/app
