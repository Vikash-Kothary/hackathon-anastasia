FROM python:3.6

ENV PIPENV_VENV_IN_PROJECT=true
ENV PIP_NO_CACHE_DIR=true

#RUN apk add --no-cache bash

RUN mkdir /app
WORKDIR /app

COPY Makefile ./
COPY requirements.txt ./
COPY src ./app/src

RUN pip install -r requirements.txt
CMD ["python", "src/main.py"]
