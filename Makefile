install:
	pip install --upgrade pip &&\
		pip install poetry &&\
			poetry install --no-root

test:
	poetry run pytest -vv

format:
	poetry run black *.py

lint:
	poetry run pylint --disable=R,C hello.py

all: install lint format test