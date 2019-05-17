.PHONY: build start stop frontend backend
#########################################

build:
	docker-compose build
start:
	docker-compose up -d
stop:
	docker-compose down
frontend:
	docker-compose run frontend sh
backend:
	docker-compose run backend

