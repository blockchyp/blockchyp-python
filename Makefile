# Executables
DOCKER = docker
PYLINT = pylint
PYTHON = python
TOX = $(PYTHON) -m tox
TWINE = twine

# Integration test config
IMAGE := python:3.7-buster
DOCKERHOME := /root
WORKSPACE := /tmp/workspace
CACHE := $(HOME)/.local/share/blockchyp/itest-cache
CONFIGFILE := sdk-itest-config.json
CERTFILE := blockchyp.crt
LICENSEFILE := LICENSE
HOSTCONFIGFILE := $(HOME)/.config/blockchyp/$(CONFIGFILE)
HOSTCERTFILE := blockchyp/resources/$(CERTFILE)
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
		$(PYTHON) -c "import tox" || $(PYTHON) -m pip install --user tox ; \
		$(TOX) -e itest -- $(if $(TEST),-k $(TEST),-m itest), \
		mkdir -p $(CACHE) ; \
		sed 's/localhost/$(HOSTIP)/' $(HOSTCONFIGFILE) >$(CACHE)/$(CONFIGFILE) ; \
		/bin/cp $(HOSTCERTFILE) $(CACHE)/$(CERTFILE) ; \
		/bin/cp $(LICENSEFILE) $(CACHE)/$(LICENSEFILE) ; \
		$(DOCKER) run \
		-v $(shell pwd):$(WORKSPACE):Z \
		-v $(CACHE)/python3.7:$(DOCKERHOME)/.local:Z \
		-v $(CACHE)/$(CERTFILE):$(WORKSPACE)/$(HOSTCERTFILE):Z \
		-v $(CACHE)/$(CONFIGFILE):$(DOCKERHOME)/.config/blockchyp/sdk-itest-config.json:Z \
		-v $(CACHE)/$(LICENSEFILE):$(WORKSPACE)/$(LICENSEFILE) \
		-v $(CACHE)/.tox:$(WORKSPACE)/.tox \
		-e BC_TEST_DELAY=$(BC_TEST_DELAY) \
		-w $(WORKSPACE) \
		--rm -it $(IMAGE) \
		$(MAKE) LOCALBUILD=1 TEST=$(TEST) integration)

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
