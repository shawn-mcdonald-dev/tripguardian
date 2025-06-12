# Constants
PORT = 8000

# Run the app using uvicorn (inside the Dev Container)
run:
	uvicorn app.main:app --host 0.0.0.0 --port $(PORT)

# Run tests using pytest (inside the Dev Container)
test:
	pytest

# Reinstall dependencies (inside the Dev Container)
install:
	pip install --no-cache-dir -r requirements.txt

# Rebuild requirements.txt from pipenv/poetry/etc. (optional)
freeze:
	pip freeze > requirements.txt
