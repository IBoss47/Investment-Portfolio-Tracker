set-up:
	docker-compose up -d

migrate:
	uv run alembic revision --autogenerate -m "$(m)"
	uv run alembic upgrade head