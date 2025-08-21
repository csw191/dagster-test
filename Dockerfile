FROM python:3.12-slim
 
# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
 
# Install Poetry
RUN pip install poetry==1.8.3
 
# Configure Poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VENV_IN_PROJECT=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache
 
WORKDIR /app
 
# Copy Poetry files
COPY pyproject.toml poetry.lock ./
 
# Install dependencies
RUN poetry install --only=main && rm -rf $POETRY_CACHE_DIR
 
# Copy application code
COPY . .
 
# Set PATH
ENV PATH="/app/.venv/bin:$PATH"
 
EXPOSE 3000
 
# Change the CMD to use Poetry to run Dagster
CMD ["poetry", "run", "dagster", "dev", "-h", "0.0.0.0", "-p", "3000"]
