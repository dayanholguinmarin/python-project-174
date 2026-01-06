lint:
	flake8 gendiff

install:
	pip install -r requirements.txt

prepare-dev:
	pip install -r requirements-dev.txt

test:
	pytest --maxfail=1 --disable-warnings
