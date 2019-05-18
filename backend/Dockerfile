FROM python:3.7-alpine

ENV PIPENV_VENV_IN_PROJECT=true
ENV PIP_NO_CACHE_DIR=true

RUN apk add --no-cache bash bash-completion make

WORKDIR /root/

# Upgrade to latest version of pip.
RUN pip install --upgrade pip && pip install pipenv

# Copy and install all pip (python) requirements.
COPY Pipfile.lock ./
RUN pipenv install

COPY Makefile ./
CMD ["/usr/bin/make", "run"]
