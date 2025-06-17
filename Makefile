# Project constants
IMAGE_NAME = tripguardian
CONTAINER_NAME = tripguardian-container
PORT = 8000

# Build Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
run:
	docker run -d --rm -p $(PORT):$(PORT) \
	-e AVIATIONSTACK_KEY="$(AVIATIONSTACK_KEY)" \
	-e RAPIDAPI_KEY="$(RAPIDAPI_KEY)" \
	--name $(CONTAINER_NAME) $(IMAGE_NAME)

debug:
	docker run -it --rm -p $(PORT):$(PORT) \
	-e AVIATIONSTACK_KEY="$(AVIATIONSTACK_KEY)" \
	-e RAPIDAPI_KEY="$(RAPIDAPI_KEY)" \
	--name $(CONTAINER_NAME) $(IMAGE_NAME)

# Stop the running container
stop:
	docker stop $(CONTAINER_NAME)

# View container logs
logs:
	docker logs -f $(CONTAINER_NAME)

# Run tests using pytest (inside the container)
test:
	docker run --rm $(IMAGE_NAME) pytest

# Clean up local containers/images (dangerous: don't run in prod)
clean:
	docker rm -f $(CONTAINER_NAME) 2>/dev/null || true
	docker rmi $(IMAGE_NAME) 2>/dev/null || true

# Rebuild from scratch
rebuild: clean build

# Build and run (local dev)
start: build run

dev: rebuild run test

# for notebook experiments
notebook:
	docker run -it --rm -p 8888:8888 -v $(PWD):/app $(IMAGE_NAME) \
	jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --notebook-dir=/app/notebooks

.PHONY: build run stop logs test clean rebuild start dev notebook