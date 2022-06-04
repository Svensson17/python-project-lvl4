package-install:
	poetry install

lint:
	poetry run flake8 .

test:
	poetry run python manage.py test

test-coverage:
	poetry run --source='.' manage.py test
	poetry run coverage report
	poetry run coverage xml
