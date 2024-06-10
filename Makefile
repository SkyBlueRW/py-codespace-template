install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora

test:
	python -m pytest -vv --cov=hello --cov=hellocli test_hello.pytest

lint:
	pylint --disable=R,C hello.py hellocli.pylint

all: install test lint