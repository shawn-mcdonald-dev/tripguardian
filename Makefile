# Constants
PROJECT_NAME = tripguardian
COMPOSE = docker compose

# Commands
.PHONY: build up down restart logs frontend backend open-notebook notebook test shell clean

build:
	$(COMPOSE) build

up:
	$(COMPOSE) up --build -d

down:
	$(COMPOSE) down

restart: down up

logs:
	$(COMPOSE) logs -f

frontend:
	xdg-open http://localhost:8501 || open http://localhost:8501

backend:
	xdg-open http://localhost:8000/docs || open http://localhost:8000/docs

open-notebook:
	xdg-open http://localhost:8888 || open http://localhost:8888

notebook:
	$(COMPOSE) up notebook

test:
	$(COMPOSE) exec backend pytest

shell:
	$(COMPOSE) exec backend /bin/bash

clean:
	docker system prune -f
