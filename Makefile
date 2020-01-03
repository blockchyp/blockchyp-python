# Executables
DOCKER = docker
PYTHON = python
PYLINT = $(PYTHON) -m pylint
TOX = $(PYTHON) -m tox
TWINE = $(PYTHON) -m twine

# Integration test config
export BC_TEST_DELAY := 5
IMAGE := python:3.7-buster
SCMROOT := $(shell git rev-parse --show-toplevel)
PWD := $(shell pwd)
CACHE := $(HOME)/.local/share/blockchyp/itest-cache
CONFIGFILE := $(HOME)/.config/blockchyp/sdk-itest-config.json
CACHEPATHS := $(dir $(CONFIGFILE)) $(HOME)/.local $(HOME)/.cache $(HOME)/.tox
ifeq ($(shell uname -s), Linux)
HOSTIP = $(shell ip -4 addr show docker0 | grep -Po 'inet \K[\d.]+')
else
HOSTIP = host.docker.internal
endif

# Default target
.PHONY: all
all: clean build test

# Cleans build artifacts
.PHONY: clean
clean:
	$(RM) -rf build dist

# Compiles the package
.PHONY: build
build: lint
	$(PYTHON) setup.py sdist

# Runs unit tests
.PHONY: test
test:
	$(TOX)

# Runs integration tests
.PHONY: integration
integration:
	$(if $(LOCALBUILD), \
		$(TOX) -e itest -- $(if $(TEST),-k $(TEST),-m itest), \
		$(foreach path,$(CACHEPATHS),mkdir -p $(CACHE)/$(path) ; ) \
		sed 's/localhost/$(HOSTIP)/' $(CONFIGFILE) >$(CACHE)/$(CONFIGFILE) ; \
		$(DOCKER) run \
		-u $(shell id -u):$(shell id -g) \
		-v $(SCMROOT):$(SCMROOT):Z \
		-v /etc/passwd:/etc/passwd:ro \
		$(foreach path,$(CACHEPATHS),-v $(CACHE)/$(path):$(path):Z) \
		-e BC_TEST_DELAY=$(BC_TEST_DELAY) \
		-e HOME=$(HOME) \
		-w $(PWD) \
		--rm -it $(IMAGE) \
		bash -c "$(PYTHON) -m pip install --user tox && $(TOX) -e itest -- $(if $(TEST),-k $(TEST),-m itest)")

# Performs any tasks necessary before a release build
.PHONY: stage
stage:

# Publish packages
.PHONY: publish
publish:
	$(TWINE) check dist/*
	$(TWINE) upload dist/*

# Run pylint
.PHONY: lint
lint:
	$(PYLINT) blockchyp
