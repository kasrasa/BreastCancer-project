install:
	pip install --upgrade pip &&\
	poetry install --no-root

test:
	poetry run pytest -vv

format:
	black *.py

lint:
	pylint --disable=R,C hello.py

all: install lint format test