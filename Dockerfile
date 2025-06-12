# Use slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (add git here)
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port FastAPI will run on
EXPOSE 8000

# Command to run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

