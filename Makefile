# Identify Operating System
ifeq ($(OS),Windows_NT)
    OPEN := start
else
    UNAME := $(shell uname -s)
    ifeq ($(UNAME),Linux)
        OPEN := xdg-open
    else
        OPEN := open
    endif
endif

-include .env
export DOCKER_BUILDKIT=1
export COMPOSE_DOCKER_CLI_BUILD=1



.PHONY: help install-poetry poetry-shell install lock-noupdate pre-commit api-tests build-tests dockerized-tests teardown-tests

help:
	@echo "Please use 'make <target>' where <target> is one of the following:"
	@echo "  install-poetry     to install poetry"
	@echo "  poetry-shell       to spawn a poetry virtual environment"
	@echo "  install-deps       to install poetry dependencies"
	@echo "  lock-noupdate      to generate/update poetry.lock without updating irrelevant dependencies"
	@echo "  pre-commit         to run pre-commit checks"
	@echo "  run-tests          to run tests"


install-poetry:
	pip install -r poetry-requirements.txt

poetry-shell:
	poetry shell

install-deps:
	poetry install --no-root

lock-noupdate:
	poetry lock --no-update

pre-commit:
	poetry run pre-commit run --all-files

run-tests:
	poetry run pytest tests
