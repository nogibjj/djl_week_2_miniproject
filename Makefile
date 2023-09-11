all: install test format lint 

install:
	python3 -m pip install --upgrade pip 
	python3 -m 	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py 

lint:
	#disable comment to test speed
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	#ruff linting is 10-100X faster than pylint
	#ruff check *.py mylib/*.py

plot:
	python3 source/main.py

#container-lint:
#	docker run --rm -i hadolint/hadolint < Dockerfile

#refactor: format lint

#deploy:
	#deploy goes here
