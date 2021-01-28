SHELL:=/bin/bash
PROJECT=project
VERSION=3.7.4
VENV=${PROJECT}-${VERSION}
VENV_DIR=$(shell pyenv root)/versions/${VENV}
PYTHON=${VENV_DIR}/bin/python
UNAME := $(shell uname)

# .ONESHELL:
.PHONY: run clean build venv tests all

ccend=$(shell tput sgr0)
ccbold=$(shell tput bold)
ccgreen=$(shell tput setaf 2)
ccso=$(shell tput smso)

clean:
	@echo ""
	@echo "$(ccso)--> Removing virtual environment $(ccend)"

	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete
	find . -type f -name '*.pid' -delete
	find . -type d -name '__pycache__' -delete

	pyenv virtualenv-delete --force ${VENV}
	rm .python-version

install-pyenv:
	@echo "Install pyenv and pyenv-virtualenv on Linux or MacOS"
	$(MAKE) $(UNAME)

Darwin: 
	brew update 
	brew install pyenv pyenv-virtualenv
	$(MAKE) fix_bash_profile

Linux: 
	git clone https://github.com/pyenv/pyenv.git ~/.pyenv
	echo 'export PYENV_ROOT="$$HOME/.pyenv"' >> ~/.bash_profile
	echo 'export PATH="$$PYENV_ROOT/bin:$$PATH"' >> ~/.bash_profile
	git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
	
	$(MAKE) fix_bash_profile

fix_bash_profile:
	echo 'eval "$$(pyenv init -)"' >> ~/.bash_profile
	echo 'eval "$$(pyenv virtualenv-init -)"' >> ~/.bash_profile
	. ~/.bash_profile

build:
	@echo ""
	@echo "$(ccso)--> Build $(ccend)"
	$(MAKE) install

venv: $(VENV_DIR)

$(VENV_DIR):
	@echo "$(ccso)--> Install and setup pyenv and virtualenv $(ccend)"
	pyenv virtualenv ${VERSION} ${VENV}
	echo ${VENV} > ./.python-version

install: venv
	@echo "$(ccso)--> Updating packages $(ccend)"
	pip install --upgrade pip
	pip install --upgrade setuptools
	python app/setup.py install

test:
	pytest app/tests

run:
	python app/run.py

travis_test:
	pip install -r requirements.txt
	pytest app/tests