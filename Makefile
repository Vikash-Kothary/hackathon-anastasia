#!make
#@ Makefile for Anastasia

#@ Commands:
.PHONY: help build start stop frontend backend


FRONTEND_CONTEXT := frontend
-include ${FRONTEND_CONTEXT}/Makefile
BACKEND_CONTEXT := backend
-include ${BACKEND_CONTEXT}/Makefile
WIKI_CONTEXT := wiki
-include ${WIKI_CONTEXT}/Makefile

-include .env
export

#@ - help: Show all commands.
help:
	@fgrep -h "#@ " $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/#@ //'

#@ - init: Download all dependencies
init:
	@docker-compose pull

#@ - build: Build app
build:
	@docker-compose build

#@ - start: Run apps
start:
	@docker-compose up -d

#@ - stop: Stop apps
stop:
	@docker-compose down

#@ - debug: Debug apps
debug:
	@docker-compose run --service-ports backend sh
