#!make
#@ Makefile for Anastasia Backend

#@ Commands:
.PHONY: help-backend init-backend lint-backend build-backend test-backend run-backend develop-backend clean-pyc clean-build
SHELL := /bin/bash
BACKEND_CONTEXT := $(or $(BACKEND_CONTEXT),.)

-include ${BACKEND_CONTEXT}/.env
export

# Allow help to be overriden by project Makefile
%: %-backend
	@true

#@ - help-backend: Show all commands.
help-backend:
	@fgrep -h "#@ " $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/#@ //'

#@ - init-backend: Install requirements.
init-backend:
	@cd ${BACKEND_CONTEXT}/ && \
	pipenv install --dev

lint-backend:
	@cd ${BACKEND_CONTEXT}/ && \
	pipenv run \
	python -m flake8

#@ - run-backend: Run backend.
run-backend:
	@cd ${BACKEND_CONTEXT}/ && \
	pipenv run \
	python src/main.py

#@ - test-backend: Run tests.
test-backend: lint-backend

#@ - develop-backend: Run jupyter notebook.
develop-backend:
	@cd ${BACKEND_CONTEXT}/ && \
	pipenv run \
	jupyter lab --notebook-dir=./notebooks

export-development-backend:
	@cd ${BACKEND_CONTEXT}/ && \
	pipenv run \
	jupyter nbconvert --to script development.ipynb
#@ 
t