FROM python:3.12-alpine


WORKDIR /crud_app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /crud_app/
