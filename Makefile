

SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules


usage:
	@echo "Usage:"
	@sed -ne 's/^/  /;/@sed/!s/## //p' $(MAKEFILE_LIST)


run-with-defaults: export DEBUG=True
run-with-defaults:	## Run a local webserver
	./manage.py runserver


test:	## Run the full test suite
	pyflakes .
	./manage.py test
