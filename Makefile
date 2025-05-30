test:
	poetry run pytest -vv

format:
	black *.py

lint:
	pylint --disable=R,C hello.py

all: lint format test