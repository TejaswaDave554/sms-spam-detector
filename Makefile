.PHONY: install train test run clean docker-build docker-run

install:
	pip install -r requirements.txt
	python -m nltk.downloader stopwords punkt

install-dev:
	pip install -r requirements-dev.txt
	python -m nltk.downloader stopwords punkt

train:
	python train_model.py

test:
	pytest tests/ -v --cov=app

run:
	python app.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -f .coverage

docker-build:
	docker build -t sms-spam-detector .

docker-run:
	docker-compose up -d

docker-stop:
	docker-compose down

lint:
	flake8 app.py train_model.py --max-line-length=120
