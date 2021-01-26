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
	pyenv virtualenv-delete --force ${VENV}
	rm .python-version

	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete
	find . -type f -name '*.pid' -delete
	find . -type d -name '__pycache__' -delete
	find . -type d -name '.coverage' -delete
	find . -type d -name '.pytest_cache' -delete

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
	python3 -m pip install --upgrade pip
	pyenv virtualenv ${VERSION} ${VENV}
	echo ${VENV} > .python-version

install: venv requirements.txt
	@echo "$(ccso)--> Updating packages $(ccend)"
	$(PYTHON) -m pip install -r requirements.txt

travis_build:
	@echo ""
	@echo "$(ccso)--> Build for travis $(ccend)"
	$(MAKE) travis_install

travis_install:
	@echo "$(ccso)--> Updating packages $(ccend)"
	pip install -r requirements.txt

tests:
	python src/app.py test

run:
	python src/app.py run

travis_test: travis_build tests