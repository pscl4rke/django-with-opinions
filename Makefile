

SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules


usage:
	@echo "Usage:"
	@sed -ne 's/^/| /;/@sed/!s/## //p' $(MAKEFILE_LIST) | (column -tl3 || cat)


run-with-defaults: export DATABASE ?= sqlite3:db.sqlite3
run-with-defaults: export DEBUG ?= True
run-with-defaults: ## Migrate local db and run a webserver from it
	./manage.py migrate
	./manage.py runserver


test: export DATABASE ?= sqlite3::memory:
test: ## Run the full test suite
	pyflakes .
	mypy .
	coverage run ./manage.py test
	coverage report -m --skip-covered


migrations: export DATABASE ?= sqlite3::memory:
migrations: ## Create any new migration files
	./manage.py makemigrations
