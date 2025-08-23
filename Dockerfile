FROM python:3.12-slim
 
# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Add these lines to your Dockerfile
RUN mkdir -p /root/.dbt
RUN mkdir -p /opt/dagster/dagster_home
RUN mkdir -p /home/jparep/proj/dbt/dagster-test/dagster_home

RUN cat > /root/.dbt/profiles.yml << 'EOF' && \
default: \
  outputs: \
    dev: \
      type: snowflake \
      account: "{{ env_var('SNOWFLAKE_ACCOUNT') }}" \
      user: "{{ env_var('SNOWFLAKE_USER') }}" \
      password: "{{ env_var('SNOWFLAKE_PASSWORD') }}" \
      role: "{{ env_var('SNOWFLAKE_ROLE') }}" \
      warehouse: "{{ env_var('SNOWFLAKE_WAREHOUSE') }}" \
      database: "{{ env_var('SNOWFLAKE_DATABASE') }}" \
      schema: "{{ env_var('SNOWFLAKE_SCHEMA') }}" \
  target: dev \
EOF




# Install Poetry
RUN pip install poetry==1.8.3
 
# Configure Poetry to NOT create virtual environment
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VENV_IN_PROJECT=0 \
    POETRY_CACHE_DIR=/tmp/poetry_cache
 
WORKDIR /app
 
# Copy Poetry files
COPY pyproject.toml poetry.lock ./
 
# Install dependencies globally (no venv)
RUN poetry config virtualenvs.create false && \
    poetry install --only=main && \
    rm -rf $POETRY_CACHE_DIR



# Copy application code
COPY . .
 
EXPOSE 3000
 
# Run dagster directly (no poetry run needed)
CMD ["dagster", "dev", "-h", "0.0.0.0", "-p", "3000"]
