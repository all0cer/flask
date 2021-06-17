install:
	pip install -e .['dev']

test:
	pytest tests/ -v

start-db:
	FLASK_APP:delivery/app.py flask create-db 
	FLASK_APP:delivery/app.py flask db upgrade 