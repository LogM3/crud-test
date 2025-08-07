run:
	uvicorn app.main:app --reload

makemigrations:
	alembic revision --autogenerate

migrate:
	alembic upgrade head
