install:
	pip install --upgrade pip &&\
	pip install poetry &&\
	poetry install --no-root
	source /home/runner/.cache/pypoetry/virtualenvs/breastcancer-project-x4a0bdNK-py3.12/bin/activate

test:
	poetry run pytest -vv

format:
	black *.py

lint:
	pylint --disable=R,C hello.py

all: install lint format test