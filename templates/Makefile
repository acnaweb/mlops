# Makefile para facilitar comandos do projeto

install:
	pip install -r requirements.txt

train:
	python src/train.py

test:
	pytest tests/

docker-build:
	docker build -t cd4ml-app .

docker-run:
	docker run --rm -v $(PWD):/app cd4ml-app

monitor:
	python src/monitor_drift.py