run:
	uvicorn app.main:app --reload

requirements:
	pip freeze > requirements.txt
