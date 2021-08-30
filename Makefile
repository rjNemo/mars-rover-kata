run:
	pipenv run python -m rover.main
test: tests
tests:
	pipenv run pytest -v --cov=. --cov-report=html
lint:
	pipenv run black -l 99 .
	pipenv run flake8 .
	pipenv run mypy .

.PHONY: run test tests lint