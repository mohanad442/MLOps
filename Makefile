install:
	pip install -r requirements.txt

lint:
	pylint --disable R,C Multiply_two_variables.py

test:
	python -m pytest -vv test_xy.py	

deploy:
	uvicorn app:app --reload