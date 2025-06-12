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

# for notebook experiments
notebook:
	docker run -it --rm -p 8888:8888 -v $(PWD):/app $(IMAGE_NAME) \
	jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --notebook-dir=/app/notebooks

.PHONY: run test install freeze notebook
